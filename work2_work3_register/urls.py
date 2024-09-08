from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name='work2_work3_register'

urlpatterns = [
    path('', views.index),
    path('api/check_name/', views.check_name),  # 作業二
    path('api/register/', views.register),  # 作業三
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
