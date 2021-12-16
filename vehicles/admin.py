from django.contrib import admin
from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'registration',
        'make',
        'model',
        'trim',
        'colour',
        'fuel',
        'engine_size',
        'body_type',
        'gearbox',
        'drivetrain',
        'seats',
        'description',
        'price',
        'mileage',
        'model_year',
        'doors',
        'images',
    )

    ordering = ('sku',)


# Register your models here.
admin.site.register(Vehicle, VehicleAdmin)