from django.db import models
from django.conf import settings
from operator import attrgetter

class VehicleImages(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    vehicle_name = models.ForeignKey('Vehicle', null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True, upload_to='vehicles/')


class Vehicle(models.Model):
    sku = models.CharField(max_length=9, null=False, blank=False)
    name = models.CharField(max_length=254, null=False, blank=False)
    registration = models.CharField(max_length=254, null=False, blank=False)
    make = models.CharField(max_length=50, null=False, blank=False)
    model = models.CharField(max_length=50, null=False, blank=False)
    trim = models.CharField(max_length=50, null=False, blank=False)
    colour = models.CharField(max_length=50, null=False, blank=False)
    fuel = models.CharField(max_length=20, null=False, blank=False)
    engine_size = models.DecimalField(max_digits=3, decimal_places=1, null=False, blank=False)
    body_type = models.CharField(max_length=15, null=False, blank=False)
    gearbox = models.CharField(max_length=15, null=False, blank=False)
    drivetrain = models.CharField(max_length=10, null=False, blank=False)
    seats = models.IntegerField(null=False, blank=False)
    description = models.TextField()
    price = models.IntegerField(null=False, blank=False)
    mileage = models.IntegerField(null=False, blank=False)
    model_year = models.IntegerField(null=False, blank=False)
    doors = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

    
class unique_vehicle_parameters():

    def unique_vehicle_makes():
        """
        Gets all the unique vehicle makes
        """
        vehicles = Vehicle.objects.all()
        vehicle_makes = []
        vehicle_makes.clear()

        for vehicle in vehicles:
            if vehicle.make not in vehicle_makes:
                vehicle_makes.append(vehicle.make)

        return vehicle_makes


    def unique_vehicle_models():
        """
        Gets the unique vehicle models with make
        """
        vehicles = Vehicle.objects.all()
        vehicle_models = []
        vehicle_models.clear()

        all_values = [value for elem in vehicle_models for value in elem.values()]

        for vehicle in vehicles:

            all_values = [value for elem in vehicle_models for value in elem.values()]
            if vehicle.model not in all_values:
                vehicle_models.append({
                    'make': vehicle.make,
                    'model': vehicle.model
                    },
                )

        return vehicle_models
