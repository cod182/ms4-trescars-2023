from django.db import models


class Vehicles(models.Model):
    sku = models.CharField(max_length=9, null=True, blank=True)
    registration = models.CharField(max_length=10)
    make = models.CharField((max_length=30)
    model = models.CharField((max_length=50)
    trim = models.CharField((max_length=30)
    colour = models.CharField((max_length=50)
    fuel = models.CharField((max_length=30)
    engine_size = models.DecimalField(..., max_digits=5, decimal_places=1)
    body_type = models.CharField((max_length=15)
    gearbox = models.CharField((max_length=15)
    drivetrain = models.CharField((max_length=30)
    seats = models.IntegerField(max_digits=30 blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=3, decimal_places=2)
    mileage = models.IntegerField(max_digits=6 blank=True, null=True)
    model_year = models.IntegerField(max_digits=4 blank=True, null=True)
    doors = models.IntegerField(max_digits=2 blank=True, null=True)
    images = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name