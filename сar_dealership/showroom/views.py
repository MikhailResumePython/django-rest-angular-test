from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from showroom.models import Car, Manufacturer, Brand
from showroom.serializers import CarSerializer, ManufacturerSerializer, BrandSerializer, InfoSerializer


class CarListPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response(OrderedDict([
             ('page_count', self.page.paginator.num_pages),
             ('page_size', self.page_size),
             ('current', self.page.number),
             ('next', self.get_next_link()),
             ('previous', self.get_previous_link()),
             ('results', data)
         ]))
    

class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    pagination_class = CarListPageNumberPagination

    def get_queryset(self):
        queryset = Car.objects.all()

        manufacturer = self.request.query_params.get('manufacturer', None)
        brand = self.request.query_params.get('brand', None)
        order = self.request.query_params.get('order_by', None)

        if manufacturer is not None:
            manufacturer_id = Manufacturer.objects.get(name__iexact=manufacturer)
            queryset = queryset.filter(manufacturer=manufacturer_id)
        if brand is not None:
            brand_id = Brand.objects.get(name__iexact=brand)
            queryset = queryset.filter(brand=brand_id)
        if order is not None:
            if order == 'min_price':
                queryset = queryset.order_by('price')
            elif order == 'max_price':
                queryset = queryset.order_by('-price')
            
        return queryset


class CarInfoViewSet(viewsets.ViewSet):
    def list(self, request):
        info = {
            'manufacturers': Manufacturer.objects.all(),
            'brands': Brand.objects.all(),
        }
        serializer = InfoSerializer(info)
        return Response(serializer.data)


class OrderViewSet(viewsets.ViewSet):
    def list(self, request):
        info = {
            
        }
        return Response(info)