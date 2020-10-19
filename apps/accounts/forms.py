from django import forms
from django.contrib.auth import get_user_model

from accounts.auth_backend.auth_backends import get_user_class_as_role
from accounts.models import Role

User = get_user_model()


class UserForm(forms.Form):
    role = forms.ChoiceField(choices=Role.choices)
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    user_class = None

    def clean_role(self):
        role = self.cleaned_data.get('role')
        if role in Role:
            self.user_class = get_user_class_as_role(role)
            return role
        else:
            raise forms.ValidationError('Unkown role')

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")
        return password

    def _get_user(self):
        username = self.cleaned_data.get('username')
        return self.user_class.objects.filter(username=username).first()


class UserLoginForm(UserForm):
    def clean_username(self):
        user = self._get_user()
        if not user:
            raise forms.ValidationError('does not exist user')
        return user.username


class UserCreateForm(UserForm):
    email = forms.EmailField(label='Email address')
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        user = self._get_user()
        if user:
            raise forms.ValidationError('this username has already been registered')
        return self.cleaned_data.get('username')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = self.user_class.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('this email has already been registered')
        return email

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords must match")
        return password2
