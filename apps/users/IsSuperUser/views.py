from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRoleToggleView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if user.is_superuser:
            user.is_superuser = False
            user.is_staff = False
        else:
            user.is_superuser = True
            user.is_staff = True
        user.save()
        return Response({'message': 'User role updated successfully'}, status=status.HTTP_200_OK)