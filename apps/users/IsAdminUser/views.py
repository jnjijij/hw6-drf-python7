from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()

class UserToggleActiveView(APIView):
    permission_classes = [IsAdminUser]

    def put(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if user.is_active:
            user.is_active = False
        else:
            user.is_active = True
        user.save()
        return Response({'message': 'User active status updated successfully'}, status=status.HTTP_200_OK)