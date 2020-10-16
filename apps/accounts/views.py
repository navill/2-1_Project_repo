from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserCreateForm, UserLoginForm
from accounts.models import NormalUser


def create_normal_user(request):
    title = "Register"
    form = UserCreateForm(request.POST or None)
    next_page = request.GET.get('next')
    if form.is_valid():
        del form.cleaned_data['password2']
        user = form.user_class(**form.cleaned_data)
        user.set_password(user.password)
        user.save()
        new_user = authenticate(username=user.username, password=user.password, role=user.role)
        login(request, new_user)
        if next_page:
            return redirect(next_page)
        return redirect("/")

    context = {
        "form": form,
        "title": title
    }

    return render(request, "base_form.html", context)


def list_normal_user(request):
    title = 'User List'
    queryset = NormalUser.objects.all()
    context = {
        'user': request.user,
        "object_list": queryset,
        "title": title,
    }
    return render(request, "user_list.html", context)


def login_view(request):
    next_page = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        role = form.cleaned_data.get('role')
        user = authenticate(username=username, password=password, role=role)
        login(request, user)
        if next_page:
            return redirect(next_page)
        return redirect("/")
    return render(request, "base_form.html", {"form": form, "title": title})


def logout_view(request):
    logout(request)
    return redirect("/")
