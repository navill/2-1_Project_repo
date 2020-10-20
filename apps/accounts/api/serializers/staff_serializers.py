from rest_framework.serializers import ModelSerializer

from accounts.models import StaffUser


class StaffCreateSerializer(ModelSerializer):
    class Meta:
        model = StaffUser
        fields = '__all__'


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