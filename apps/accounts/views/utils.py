from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import redirect


def staff_login_required(function):
    def wrapper(request, *args, **kwargs):
        user_info = request.session.get('user_info')
        role = None
        if user_info:
            user_id, role = decode_user_info(user_info)

        if not (request.user.is_authenticated and role == 'Staff'):
            return redirect('login')
        else:
            return function(request, *args, **kwargs)

    return wrapper


def encode_user_info(user_id, role):
    user_info = [str(user_id), '_', role]
    return ''.join(user_info)


def decode_user_info(user_info):
    try:
        user_id, role = user_info.split('_')
    except ValueError:
        return HttpResponse('invalid user info')
    return user_id, role


def do_login(request, username, password, role):
    user = authenticate(username=username, password=password, role=role)
    login(request, user)


def add_info_to_session(request, username, role):
    user_info = encode_user_info(username, role)
    request.session['user_info'] = user_info
    return request
