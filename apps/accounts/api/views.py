from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *


class NormalUserCreateView(CreateModelMixin, GenericAPIView):
    serializer_class = None


class NormalUserListView(ListModelMixin, GenericAPIView):
    serializer_class = None


class NormalUserRetrieveView(RetrieveModelMixin, GenericAPIView):
    serializer_class = None


class NormalUserDeleteView(DestroyModelMixin, GenericAPIView):
    serializer_class = None


class StaffUserCreateView(CreateModelMixin, GenericAPIView):
    serializer_class = None


class StaffUserListView(ListModelMixin, GenericAPIView):
    serializer_class = None


class StaffUserRetrieveView(RetrieveModelMixin, GenericAPIView):
    serializer_class = None


class StaffUserDeleteView(DestroyModelMixin, GenericAPIView):
    serializer_class = None


