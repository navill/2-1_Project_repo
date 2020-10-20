from rest_framework.serializers import ModelSerializer

from accounts.models import NormalUser


class NormalCreateSerializer(ModelSerializer):
    class Meta:
        model = NormalUser
        fields = '__all__'


class NormalListSerializer(ModelSerializer):
    class Meta:
        model = NormalUser
        fields = '__all__'


class NormalRetrieveUpdateSerializer(ModelSerializer):
    class Meta:
        model = NormalUser
        fields = '__all__'


class NormalDestroySerializer(ModelSerializer):
    class Meta:
        model = NormalUser
        fields = '__all__'
