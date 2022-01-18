from django.db import models
from django.conf import settings
from operator import attrgetter


class VehicleImages(models.Model):
    class Meta:
        verbose_name_plural = "Vehicle Images"

    name = models.CharField(max_length=254, null=False, blank=False)
    vehicle_name = models.ForeignKey(
        "Vehicle", null=True, blank=True, on_delete=models.CASCADE
    )
    image = models.ImageField(null=True, blank=True)
    main = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name


gearbox_choices = (
    ("manual", "Manual"),
    ("automatic", "Automatic"),
    ("semi-automatic", "Semi-Automatic"),
)

body_type_choices = (
    ("4x4", "4x4"),
    ("convertible", "Convertible"),
    ("coupe", "Coupe"),
    ("estate", "Estate"),
    ("hatchback", "Hatchback"),
    ("motorhome", "Motorhome"),
    ("mpv", "MPV"),
    ("pickup", "Pickup"),
    ("saloon", "Saloon"),
    ("suv", "SUV"),
    ("van", "Van"),
)

drivetrain_choices = (
    ("2wd", "2WD"),
    ("4wd", "4WD"),
)

fuel_choices = (
    ("petrol", "Petrol"),
    ("diesel", "Diesel"),
    ("petrol-hybrid", "Petrol-Hybrid"),
    ("diesel-hybrid", "Diesel-Hybrid"),
    ("hydrogen", "Hydrogen"),
    ("electricity", "Electricity"),
)

colour_choices = (
    ("blue", "Blue"),
    ("black", "Black"),
    ("green", "Green"),
    ("multi-coloured", "Multi-Coloured"),
    ("orange", "Orange"),
    ("pink", "Pink"),
    ("purple", "Purple"),
    ("red", "Red"),
    ("silver", "Silver"),
    ("white", "White"),
    ("yellow", "Yellow"),
)

available_choices = (("yes", "yes"), ("no", "no"))


class Vehicle(models.Model):
    sku = models.CharField(max_length=9, null=False, blank=False)
    name = models.CharField(max_length=254, null=False, blank=False)
    registration = models.CharField(max_length=254, null=False, blank=False)
    make = models.CharField(max_length=50, null=False, blank=False)
    model = models.CharField(max_length=50, null=False, blank=False)
    trim = models.CharField(max_length=50, null=False, blank=False)
    colour = models.CharField(
        max_length=50, null=False, blank=False, choices=colour_choices
    )
    fuel = models.CharField(
        max_length=20, null=False, blank=False, choices=fuel_choices
    )
    engine_size = models.DecimalField(
        max_digits=2, decimal_places=1, null=False, blank=False
    )
    body_type = models.CharField(
        max_length=15, null=False, blank=False, choices=body_type_choices
    )
    gearbox = models.CharField(
        max_length=15, null=False, blank=False, choices=gearbox_choices
    )
    drivetrain = models.CharField(
        max_length=10, null=False, blank=False, choices=drivetrain_choices
    )
    seats = models.IntegerField(null=False, blank=False)
    description = models.TextField()
    price = models.IntegerField(null=False, blank=False, default=200)
    full_price = models.IntegerField(null=False, blank=False)
    mileage = models.IntegerField(null=False, blank=False)
    model_year = models.IntegerField(null=False, blank=False)
    doors = models.IntegerField(null=False, blank=False)
    type = models.CharField(max_length=9, null=False, blank=False, default="vehicle")
    available = models.CharField(
        max_length=9, null=False, blank=False, default="yes", choices=available_choices
    )

    def __str__(self):
        return self.name
