from rest_framework import serializers
from showroom.models import Car, Manufacturer, Brand

class CarSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name')
    manufacturer = serializers.CharField(source='manufacturer.name')
    
    class Meta:
        model = Car
        fields = 'id', 'manufacturer', 'brand', 'model', 'price', 'power', 'drive', 'engine_type', 'transmission', 'image'

    

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = 'id', 'name'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = 'id', 'name'

class InfoSerializer(serializers.Serializer):
    manufacturers = ManufacturerSerializer(many=True)
    brands = BrandSerializer(many=True)