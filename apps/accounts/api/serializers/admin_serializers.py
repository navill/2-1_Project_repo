from rest_framework.serializers import ModelSerializer

from accounts.models import AdminUser


class AdminCreateSerializer(ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'


class AdminListSerializer(ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'


class AdminRetrieveUpdateSerializer(ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'


class AdminDestroySerializer(ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'
