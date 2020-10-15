from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import UserCreateForm, UserLoginForm
from accounts.models import NormalUser


def create_normal_user(request):
    title = "Register"
    form = UserCreateForm(request.POST or None)
    next_page = request.GET.get('next')

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
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
        "object_list": queryset,
        "title": title,
    }
    return render(request, "user_list.html", context)


def login_view(request):
    next_page = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    print(form)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        
        user = authenticate(username=username, password=password)
        login(request, user)
        if next_page:
            return redirect(next_page)
        return redirect("/")
    return render(request, "base_form.html", {"form": form, "title": title})


def logout_view(request):
    logout(request)
    return redirect("/")
