from django.contrib import admin

from .models import Manufacturer, Brand, Car

admin.site.register(Manufacturer)
admin.site.register(Brand)
admin.site.register(Car)
