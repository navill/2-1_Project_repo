from __future__ import absolute_import

from typing import Dict

from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from accounts.models import NormalUser, Role


class NormalCreateSerializer(ModelSerializer):
    username = serializers.CharField(min_length=4, max_length=16, required=True,
                                     validators=[UniqueValidator(queryset=NormalUser.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=NormalUser.objects.all())])
    password = serializers.CharField(min_length=8, max_length=16, write_only=True,
                                     style={'input_type': 'password'})
    password2 = serializers.CharField(min_length=8, max_length=16, write_only=True,
                                      style={'input_type': 'password'})
    role = serializers.ChoiceField(choices=Role.choices)

    class Meta:
        model = NormalUser
        fields = ('username', 'email', 'password', 'password2', 'role')

    def create(self, validated_data: Dict) -> NormalUser:
        try:
            instance = NormalUser.objects.create_user(**validated_data)
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

    def _check_match_password(self, password1: str, password2: str) -> bool:
        if password1 != password2:
            raise Exception('password must match')
        return True


class NormalListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='accounts_api:detail_normal',
        lookup_field='pk'
    )

    class Meta:
        model = NormalUser
        exclude = ['password']


class NormalRetrieveUpdateSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='accounts_api:detail_normal',
        lookup_field='pk'
    )

    class Meta:
        model = NormalUser
        read_only_fields = ['__all__']
        exclude = ['password']


class NormalDestroySerializer(ModelSerializer):
    class Meta:
        model = NormalUser
        read_only_fields = ['username']
        exclude = ['password']
