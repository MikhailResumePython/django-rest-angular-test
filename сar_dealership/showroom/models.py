from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=64)


class Brand(models.Model):
    name = models.CharField(max_length=64)

class Car(models.Model):
    price = models.FloatField()
    power = models.IntegerField()
    seats = models.IntegerField()
    drive = models.CharField(max_length=64)
    engine_type = models.CharField(max_length=64)
    transmission = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images')
    models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    models.ForeignKey(Brand, on_delete=models.CASCADE)


