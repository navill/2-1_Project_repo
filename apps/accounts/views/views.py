from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import UserCreateForm, UserLoginForm
from accounts.models import NormalUser
from accounts.views.utils import add_info_to_session, do_login


def create_normal_user(request):
    next_page = request.GET.get('next')
    title = "Register"
    form = UserCreateForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        role = form.cleaned_data.get('role')
        del form.cleaned_data['password2']

        user = form.user_class(**form.cleaned_data)
        user.set_password(user.password)
        user.save()

        request_with_session = add_info_to_session(request, username, role)
        do_login(request_with_session, username, password, role)

        if next_page:
            return redirect(next_page)
        return redirect("/")

    context = {
        "form": form,
        "title": title
    }

    return render(request, "base_form.html", context)


def login_view(request):
    next_page = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        role = form.cleaned_data.get('role')

        request_with_session = add_info_to_session(request, username, role)
        do_login(request_with_session, username, password, role)
        if next_page:
            return redirect(next_page)

        url_as_role = f'list_{role.lower()}'
        return redirect(url_as_role)
    return render(request, "base_form.html", {"form": form, "title": title})


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def list_normal_user(request):
    title = 'User List'
    queryset = NormalUser.objects.all()
    context = {
        'user': request.user,
        "object_list": queryset,
        "title": title,
    }
    return render(request, "user_list.html", context)
