from django.urls import path

from accounts.api.views import *

app_name = 'accounts_api'

urlpatterns = [
    path('normal/list/', NormalUserListView.as_view(), name='list_normal'),
    path('normal/create/', NormalUserCreateView.as_view(), name='create_normal'),
    path('normal/detail/<int:pk>', NormalUserRetrieveUpdateView.as_view(), name='detail_normal'),
    path('normal/delete/<int:pk>', NormalUserDestroyView.as_view(), name='delete_normal'),

    path('staff/list/', StaffUserListView.as_view(), name='list_staff'),
    path('staff/create/', StaffUserCreateView.as_view(), name='create_staff'),
    path('staff/detail/<int:pk>', StaffUserRetrieveUpdateView.as_view(), name='detail_normal'),
    path('staff/delete/<int:pk>', StaffUserDestroyView.as_view(), name='delete_normal'),

    path('admin/list/', AdminUserListView.as_view(), name='list_admin'),
    path('admin/create/', AdminUserCreateView.as_view(), name='create_admin'),
    path('admin/detail/<int:pk>', AdminUserRetrieveUpdateView.as_view(), name='detail_admin'),
    path('admin/delete/<int:pk>', AdminUserDestroyView.as_view(), name='delete_admin'),
]
