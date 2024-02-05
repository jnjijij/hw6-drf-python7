from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'price', 'year', 'body_type','created_at', 'updated_at')

    def validate_brand(self, value):
        if value == 'R':
            raise ValidationError({'details': 'brand == RIO'})
        return value

    def validate(self, item):
        if item['price'] == item['year']:
            raise ValidationError({'details': 'price == year'})
        return item