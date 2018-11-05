from rest_framework import serializers
from showroom.models import Car 

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = 'id', 'manufacturer', 'brand', 'model', 'price', 'power', 'drive', 'engine_type', 'transmission', 'image'