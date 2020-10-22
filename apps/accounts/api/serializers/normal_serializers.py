from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.serializers import ModelSerializer

from accounts.models import NormalUser


class NormalCreateSerializer(ModelSerializer):
    class Meta:
        model = NormalUser
        # fields = '__all__'
        exclude = ['deleted', 'is_admin', 'is_active', 'is_superuser']

    # def create(self, validated_data):  # -> view에서 처리
    #     pass


class NormalListSerializer(ModelSerializer):
    class Meta:
        model = NormalUser
        read_only_fields = ['__all__']
        exclude = ['password']


class NormalRetrieveUpdateSerializer(ModelSerializer):
    username = serializers.CharField(read_only=True)

    class Meta:
        model = NormalUser
        # fields = '__all__'
        read_only_fields = ['__all__']
        exclude = ['password']

    # def update(self, instance, validated_data):  # -> view에서 처리
    #     pass


class NormalDestroySerializer(ModelSerializer):
    class Meta:
        model = NormalUser
        read_only_fields = ['username']
        exclude = ['password']
