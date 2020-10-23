from typing import Dict

from django.urls import reverse
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from accounts.models import StaffUser, Role


class StaffCreateSerializer(ModelSerializer):
    username = serializers.CharField(min_length=4, max_length=16, required=True,
                                     validators=[UniqueValidator(queryset=StaffUser.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=StaffUser.objects.all())])
    password = serializers.CharField(min_length=8, max_length=16, write_only=True, required=True)
    password2 = serializers.CharField(min_length=8, max_length=16, write_only=True, required=True)
    role = serializers.ChoiceField(choices=Role.choices)

    class Meta:
        model = StaffUser
        fields = ('username', 'email', 'password', 'password2', 'role')

    def create(self, validated_data: Dict) -> StaffUser:
        try:
            instance = StaffUser.objects.create_user(**validated_data)
            validated_data.pop('password')
        except Exception:
            raise
        return instance

    def validate(self, attrs: Dict) -> Dict:
        if self._check_match_password(attrs['password'], attrs['password2']):
            del attrs['password2']
        return attrs

    def to_internal_value(self, data: Dict) -> Dict:
        try:
            data = super().to_internal_value(data)  # -> ValidationError
            result = {
                'username': data['username'].lower(),
                'email': data['email'].lower(),
                'password': data['password'],
                'password2': data['password2'],
            }
        except Exception as e:
            raise
        return result

    def to_representation(self, values: Dict) -> Dict:
        return {
            'username': values['username'],
            'email': values['email'],
            'status': 'ok'
        }

    def _check_match_password(self, password1: str, password2: str) -> str:
        if password1 != password2:
            raise Exception
        return password1


class StaffListSerializer(ModelSerializer):
    class Meta:
        model = StaffUser
        fields = '__all__'


class StaffRetrieveUpdateSerializer(ModelSerializer):
    class Meta:
        model = StaffUser
        fields = '__all__'


class StaffDestroySerializer(ModelSerializer):
    class Meta:
        model = StaffUser
        fields = '__all__'

    def get_absolute_url(self):
        return reverse("accounts:detail_staff", kwargs={"pk": self.id})

    def get_api_url(self):
        return reverse("accounts_api:detail_normal", kwargs={"pk": self.id})
