from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import UserCreateForm, UserLoginForm
from accounts.models import NormalUser, Role, StaffUser
from accounts.views.utils import admin_login_required


@admin_login_required
def list_admin_view(request):
    title = 'Admin page'

    context = {
        'user': request.user,
        "object_list": 'queryset',
        "title": title,
    }
    return render(request, 'admin_list', context)
