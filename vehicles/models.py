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

    def unique_vehicle_colours():
        """
        Gets all the unique vehicle colours
        """
        vehicles = Vehicle.objects.all()
        vehicle_colours = []
        vehicle_colours.clear()

        for vehicle in vehicles:
            if vehicle.colour not in vehicle_colours:
                vehicle_colours.append(vehicle.colour)

        return sorted(vehicle_colours)

    def unique_vehicle_engines():
        """
        Gets all the unique vehicle engines
        """
        vehicles = Vehicle.objects.all()
        vehicle_engines = []
        vehicle_engines.clear()

        for vehicle in vehicles:
            if vehicle.engine_size not in vehicle_engines:
                vehicle_engines.append(vehicle.engine_size)

        return sorted(vehicle_engines)

    def unique_vehicle_doors():
        """
        Gets all the unique vehicle doors
        """
        vehicles = Vehicle.objects.all()
        vehicle_doors = []
        vehicle_doors.clear()

        for vehicle in vehicles:
            if vehicle.doors not in vehicle_doors:
                vehicle_doors.append(vehicle.doors)

        return sorted(vehicle_doors)

    def unique_vehicle_body():
        """
        Gets all the unique vehicle body
        """
        vehicles = Vehicle.objects.all()
        vehicle_body = []
        vehicle_body.clear()

        for vehicle in vehicles:
            if vehicle.body_type not in vehicle_body:
                vehicle_body.append(vehicle.body_type)

        return sorted(vehicle_body)

    def unique_vehicle_fuels():
        """
        Gets all the unique vehicle fuels
        """
        vehicles = Vehicle.objects.all()
        vehicle_fuels = []
        vehicle_fuels.clear()

        for vehicle in vehicles:
            if vehicle.fuel not in vehicle_fuels:
                vehicle_fuels.append(vehicle.fuel)

        return sorted(vehicle_fuels)

    def unique_vehicle_drivetrains():
        """
        Gets all the unique vehicle drivetrains
        """
        vehicles = Vehicle.objects.all()
        vehicle_drivetrains = []
        vehicle_drivetrains.clear()

        for vehicle in vehicles:
            if vehicle.drivetrain not in vehicle_drivetrains:
                vehicle_drivetrains.append(vehicle.drivetrain)

        return sorted(vehicle_drivetrains)

    def unique_vehicle_years():
        """
        Gets all the unique vehicle year
        """
        vehicles = Vehicle.objects.all()
        vehicle_years = []
        vehicle_years.clear()

        for vehicle in vehicles:
            if vehicle.model_year not in vehicle_years:
                vehicle_years.append(vehicle.model_year)

        return sorted(vehicle_years)