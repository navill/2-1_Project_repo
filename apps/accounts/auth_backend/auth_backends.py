import importlib
from typing import Any

from django.contrib.auth.backends import BaseBackend

from accounts.models import NormalUser, User


class UserClass:
    user_class: Any

    # @property
    # def user_class(self):
    #     return self._user_class
    #
    # @user_class.setter
    # def user_class(self, klass):
    #     self._user_class = klass


class AuthenticationBackend(BaseBackend):
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
        try:
            user_class = UserClass.user_class
            return user_class.objects.get(pk=user_id)
        except NormalUser.DoesNotExist:
            return None


def get_user_class_as_role(role):
    class_name = ''.join([role, 'User'])
    my_module = importlib.import_module("accounts.models")
    return getattr(my_module, class_name)
