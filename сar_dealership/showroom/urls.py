from django.urls import path
from rest_framework import routers

from . import views

app_name = 'showroom'


router = routers.SimpleRouter()
router.register('cars', views.CarViewSet, basename='cars')

urlpatterns = [] 