from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.models import ProfileModel
from apps.users.serializers import UserSerializer, ProfileAvatarSerializer
from django.contrib.auth import get_user_model

from core.permissions.is_admin_or_write_only_permission import IsAdminOrWriteOnlyPermission

UserModel = get_user_model()


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminOrWriteOnlyPermission,)


class MeView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UserAddAvatarView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileAvatarSerializer
    http_method_names = ('put',)

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        profile: ProfileModel = self.get_object()
        profile.avatar.delete()
        super().perform_update(serializer)