from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model

from accounts.auth_backend.auth_backends import get_user_class
from accounts.models import NormalUser, Role, StaffUser

User = get_user_model()


class UserLoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        role = self.cleaned_data.get('role')
        user_class = get_user_class(role)
        user = user_class.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError('This username has already been registered')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")
        return password


class UserCreateForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=Role.choices, widget=forms.RadioSelect())

    class Meta:
        model = NormalUser
        fields = [
            'username',
            'email',
            'password',
            'role'
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        role = self.cleaned_data.get('role')
        user_class = get_user_class(role)
        user = user_class.objects.filter(username=username)
        if user.exists():
            raise forms.ValidationError('this username has already been registered')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = NormalUser.objects.filter(email='email')
        if user.exists():
            raise forms.ValidationError('this email has already been registered')
        return email

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Passwords must match")
        return password2
