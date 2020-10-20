from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *

from accounts.api.admin_serializers import \
    AdminCreateSerializer, AdminListSerializer, AdminRetrieveUpdateSerializer, AdminDestroySerializer
from accounts.api.normal_serializers import \
    NormalCreateSerializer, NormalListSerializer, NormalRetrieveUpdateSerializer, NormalDestroySerializer
from accounts.api.staff_serializers import \
    StaffCreateSerializer, StaffListSerializer, StaffRetrieveUpdateSerializer, StaffDestroySerializer
from accounts.models import AdminUser, NormalUser, StaffUser


# Normal
class NormalUserCreateView(CreateModelMixin, GenericAPIView):
    queryset = NormalUser.objects.all()
    serializer_class = NormalCreateSerializer


class NormalUserListView(ListModelMixin, GenericAPIView):
    queryset = NormalUser.objects.all()
    serializer_class = NormalListSerializer


class NormalUserRetrieveUpdateView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = NormalUser.objects.all()
    serializer_class = NormalRetrieveUpdateSerializer
    lookup_field = 'pk'


class NormalUserDestroyView(DestroyModelMixin, GenericAPIView):
    queryset = NormalUser.objects.all()
    serializer_class = NormalDestroySerializer


# Staff
class StaffUserCreateView(CreateModelMixin, GenericAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = StaffCreateSerializer


class StaffUserListView(ListModelMixin, GenericAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = StaffListSerializer


class StaffUserRetrieveView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = StaffRetrieveUpdateSerializer
    lookup_field = 'pk'


class StaffUserDestroyView(DestroyModelMixin, GenericAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = StaffDestroySerializer


# Admin
class AdminUserCreateView(CreateModelMixin, GenericAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminCreateSerializer


class AdminUserListView(ListModelMixin, GenericAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminListSerializer


class AdminUserRetrieveUpdateView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminRetrieveUpdateSerializer
    lookup_field = 'pk'


class AdminUserDestroyView(DestroyModelMixin, GenericAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminDestroySerializer
