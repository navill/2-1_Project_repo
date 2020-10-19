from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import UserCreateForm, UserLoginForm
from accounts.models import NormalUser, Role, StaffUser