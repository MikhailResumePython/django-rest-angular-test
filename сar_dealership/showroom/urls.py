from django.urls import path
from rest_framework import routers

from . import views

app_name = 'showroom'


router = routers.SimpleRouter()
router.register('cars.get_page', views.CarViewSet, basename='cars.get_page')
router.register('cars.get_info', views.CarInfoViewSet, basename='cars.get_info')

urlpatterns = [] 