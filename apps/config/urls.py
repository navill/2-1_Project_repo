"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import create_normal_user, list_normal_user, login_view, logout_view, list_staff_user

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('create/', create_normal_user, name='create_user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('normal/', list_normal_user, name='list_normal'),
    path('staff/', list_staff_user, name='list_staff'),
]
