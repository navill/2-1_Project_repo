from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from accounts.models import Role, StaffUser, NormalUser


class AuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, role=None):
        if role == Role.NORMAL:
            try:
                user = NormalUser.objects.get(username=username)
                user.check_password(raw_password=password)
            except user.DoesNotExist:
                raise
            return user
        return None

    def get_user(self, user_id):
        try:
            return NormalUser.objects.get(pk=user_id)
        except NormalUser.DoesNotExist:
            return None

