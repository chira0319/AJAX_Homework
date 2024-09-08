"""
URL configuration for ajaxproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/
    path('', include('work1_travel.urls')),
    # http://127.0.0.1:8000/work1_travel/
    path('work1_travel/', include('work1_travel.urls')),
    # http://127.0.0.1:8000/work2_work3_register/
    path('work2_work3_register/', include('work2_work3_register.urls')),
]
