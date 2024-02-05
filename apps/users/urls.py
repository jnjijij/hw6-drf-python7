from django.urls import path

from .views import UserCreateView, UserAddAvatarView

urlpatterns = [
    path('', UserCreateView.as_view(), name='user_create'),
    path('/avatar', UserAddAvatarView.as_view(), name='user_avatar')
]