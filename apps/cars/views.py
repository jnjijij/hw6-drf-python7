from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


class CarsListCreateView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

class CarPhotoCreateView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)