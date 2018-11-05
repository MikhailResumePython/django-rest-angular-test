from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name 


class Brand(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name 


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=64)
    price = models.FloatField()
    power = models.IntegerField()
    drive = models.CharField(max_length=64)
    engine_type = models.CharField(max_length=64)
    transmission = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return str(self.brand) + ' ' + self.model


