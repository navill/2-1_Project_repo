import importlib

from django.contrib.auth.backends import BaseBackend

from accounts.models import NormalUser, User


class AuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, role=None):
        user_class = get_user_class(role)
        if user_class in User.__subclasses__():  # 이부분이 필요 할까?
            try:
                user = user_class.objects.get(username=username)
                user.check_password(password)
            except User.DoesNotExist:
                raise
            return user
        return None

    def get_user(self, user_id):
        try:
            return NormalUser.objects.get(pk=user_id)
        except NormalUser.DoesNotExist:
            return None


def get_user_class(role):
    class_name = ''.join([role, 'User'])
    my_module = importlib.import_module("accounts.models")
    return getattr(my_module, class_name)
