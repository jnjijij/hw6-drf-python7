from django.urls import path
from . import views

urlpatterns = [
    # Existing endpoints
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/update/', views.UpdateProfileView.as_view(), name='update_profile'),
    path('users/<int:user_id>/role/', views.UserRoleToggleView.as_view(), name='user-role-toggle'),
]