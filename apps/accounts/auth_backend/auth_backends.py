import importlib
from typing import Any

from django.contrib.auth.backends import ModelBackend

from accounts.models import User


class UserClass:
    user_class: Any


class AuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, role=None):
        user_class = UserClass.user_class = get_user_class_as_role(role)
        user = None
        if user_class in User.__subclasses__():  # 이부분이 필요 할까?
            try:
                user = user_class.objects.get(username=username)
                user.check_password(password)
            except user_class.DoesNotExist:
                raise
        return user

    def get_user(self, user_id):
        user_class = None
        try:
            if hasattr(UserClass, 'user_class'):
                user_class = UserClass.user_class
                return user_class.objects.get(pk=user_id)
        except user_class.DoesNotExist:
            return None


def get_user_class_as_role(role):
    class_name = ''.join([role, 'User'])
    my_module = importlib.import_module("accounts.models")
    return getattr(my_module, class_name)
