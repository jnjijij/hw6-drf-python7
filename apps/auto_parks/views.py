from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.auto_parks.models import AutoParkModel
from apps.auto_parks.serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny


class AutoParksListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer
    permission_classes = (AllowAny, )


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        auto_park = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_park=auto_park)
        ap_serializer = AutoParkSerializer(auto_park)
        return Response(ap_serializer.data, status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        auto_park = self.get_object()
        serializer = CarSerializer(auto_park.cars, many=True)
        return Response(serializer.data, status.HTTP_200_OK)