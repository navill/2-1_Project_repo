from django import forms
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model

from accounts.models import NormalUser, Role, StaffUser

User = get_user_model()


class UserLoginForm(forms.Form):
    role = forms.ChoiceField(choices=Role.choices, widget=forms.RadioSelect())
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        role = self.cleaned_data.get('role')

        # self._change_auth_model_as_role(role)

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect passsword")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super().clean()

    def _change_auth_model_as_role(self, role):
        if role == Role.STAFF:
            settings.AUTH_USER_MODEL = StaffUser
        elif role == Role.NORMAL:
            settings.AUTH_USER_MODEL = NormalUser
        else:
            raise AttributeError('Invalid role')


class UserCreateForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField(label='Email address')
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = NormalUser
        fields = [
            'username',
            'email',
            'password'
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = NormalUser.objects.filter(username=username)
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
