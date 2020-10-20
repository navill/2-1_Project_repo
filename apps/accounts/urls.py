from django.urls import path

from accounts.views.staff_view import list_staff_user
from accounts.views.views import create_normal_user, list_normal_user, login_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('create/', create_normal_user, name='create_user'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('normal/', list_normal_user, name='list_normal'),
    path('staff/', list_staff_user, name='list_staff'),
]
