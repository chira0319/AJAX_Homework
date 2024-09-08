from django.shortcuts import render
from django.http import JsonResponse
from .models import Member
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password, check_password # 密碼加鹽(亂數)套件
import re

# 透過URL顯示首頁
def index(request):
    return render(request, 'work2_work3_register/index.html')

# 作業二 
def check_name(request):
    name = request.GET.get('name', None)
    data = {
        'exists': Member.objects.filter(user_name=name).exists() # 檢查資料庫中是否有這個 name
    }
    return JsonResponse(data) # 回傳一個'key':value的結果為'exists': True or False

# 作業三
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('Inputpassword')
        password_confirm = request.POST.get('Inputpassword1')
        age = request.POST.get('age')
        avatar = request.FILES.get('avatar')

        # 若有必填欄位未填寫，依空欄顯示'message'項目
        empty_fields = []
        if not name:
            empty_fields.append('姓名')
        if not email:
            empty_fields.append('電子郵件')
        if not password:
            empty_fields.append('密碼')
        if not password_confirm:
            empty_fields.append('密碼確認')

        if empty_fields:
            return JsonResponse({
                'status': 'error',
                'message': f'註冊失敗，尚未填入{"、".join(empty_fields)}'
            })

        # 檢查電子郵件格式
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$')
        if not email_pattern.match(email):
            return JsonResponse({
                'status': 'error',
                'message': '註冊失敗，電子郵件格式不正確'
            })

        # 檢查電子郵件是否已存在
        if Member.objects.filter(user_email=email).exists():
            return JsonResponse({
                'status': 'error',
                'message': '註冊失敗，已存在相同電子郵件'
            })
        
        # 檢查密碼是否一致
        if password != password_confirm:
            return JsonResponse({'status': 'error', 'message': '註冊失敗，密碼不一致'})


        # 如以上註冊失敗都沒發生，則寫進資料庫
        try:
            # 把POST來的age賦值給user_age再使用，避免無值None報錯
            new_age = None
            if age:
                new_age = int(age)
                if new_age < 0: # 如輸入為負數視同None
                    new_age = None

            new_member = Member(    
                user_name = name,
                user_email = email,
                user_password = make_password(password), # 密碼加鹽(亂數)
                user_age = new_age,  # 使用處理後的年齡
                # user_avator = avatar # 下面avatar判斷獨立設定(new_member.user_avator = upload_file)
            )
            # 有上傳檔案才執行儲存動作
            if avatar: # avatar = request.FILES.get('avatar')
                fs = FileSystemStorage() # 將檔案保存到設定的目錄(MEDIA_ROOT)
                file_name = f'{name}_{avatar.name}' # 使用者姓名_檔名_亂數編碼(檔名重複時)
                upload_file = fs.save(file_name, avatar) #.save保存檔案的方法(前一行的檔名, .get接收的檔案)
                new_member.user_avator = upload_file # 在new_member裡補上user_avator = upload_file
            new_member.save() # 一起寫入Member資料庫
            
            return JsonResponse({'status': 'success', 'message': f'註冊成功，歡迎{name}加入'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'註冊失敗，發生未知錯誤：{str(e)}'})

    # 處理 GET 請求
    return JsonResponse({'status': 'error', 'message': '不支援的請求方法'})
