from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from rest_framework.pagination import LimitOffsetPagination

from accounts.api.serializers.admin_serializers import \
    AdminCreateSerializer, AdminListSerializer, AdminRetrieveUpdateSerializer, AdminDestroySerializer
from accounts.api.serializers.mixins import CreateUserMixin
from accounts.api.serializers.normal_serializers import \
    NormalCreateSerializer, NormalListSerializer, NormalRetrieveUpdateSerializer, NormalDestroySerializer
from accounts.api.serializers.staff_serializers import \
    StaffCreateSerializer, StaffListSerializer, StaffRetrieveUpdateSerializer, StaffDestroySerializer
from accounts.models import AdminUser, NormalUser, StaffUser


# Normal
class NormalUserCreateView(CreateUserMixin, GenericAPIView):
    serializer_class = NormalCreateSerializer

    # todo: User.objects.create_user()를 이용해 계정 생성
    # CreateUserMixin 생성 -> 각 view에 상속
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NormalUserListView(ListModelMixin, GenericAPIView):
    queryset = NormalUser.normal_manager.active_user()
    serializer_class = NormalListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NormalUserRetrieveUpdateView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = NormalUser.normal_manager.active_user()
    serializer_class = NormalRetrieveUpdateSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class NormalUserDestroyView(DestroyModelMixin, GenericAPIView):
    queryset = NormalUser.normal_manager.active_user()
    serializer_class = NormalDestroySerializer
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Staff
class StaffUserCreateView(CreateUserMixin, GenericAPIView):
    serializer_class = StaffCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StaffUserListView(ListModelMixin, GenericAPIView):
    queryset = StaffUser.staff_manager.active_staff()
    serializer_class = StaffListSerializer
    pagination_class = LimitOffsetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StaffUserRetrieveUpdateView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = StaffUser.staff_manager.active_staff()
    serializer_class = StaffRetrieveUpdateSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class StaffUserDestroyView(DestroyModelMixin, GenericAPIView):
    queryset = StaffUser.staff_manager.active_staff()
    serializer_class = StaffDestroySerializer
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Admin
class AdminUserCreateView(CreateUserMixin, GenericAPIView):
    serializer_class = AdminCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AdminUserListView(ListModelMixin, GenericAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminListSerializer
    pagination_class = LimitOffsetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AdminUserRetrieveUpdateView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminRetrieveUpdateSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class AdminUserDestroyView(DestroyModelMixin, GenericAPIView):
    queryset = AdminUser.objects.all()
    serializer_class = AdminDestroySerializer
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
