from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers

from showroom.models import Car
from showroom.serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer