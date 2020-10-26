from __future__ import absolute_import

from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer

from accounts.models import NormalUser

account_detail_url = HyperlinkedIdentityField(
    view_name='accounts-api:detail_normal',
    lookup_field='pk'
)


class NormalCreateSerializer(ModelSerializer):
    class Meta:
        model = NormalUser
        exclude = ['deleted', 'is_admin', 'is_active', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}


class NormalListSerializer(ModelSerializer):
    class Meta:
        model = NormalUser
        read_only_fields = ['__all__']
        exclude = ['password']


class NormalRetrieveUpdateSerializer(ModelSerializer):
    url = account_detail_url
    username = serializers.CharField(read_only=True)

    class Meta:
        model = NormalUser
        read_only_fields = ['__all__']
        exclude = ['password']


class NormalDestroySerializer(ModelSerializer):
    class Meta:
        model = NormalUser
        read_only_fields = ['username']
        exclude = ['password']
