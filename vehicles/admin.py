from django.contrib import admin
from .models import Vehicle, VehicleImages


class VehicleImagesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'vehicle_name',
        'image',
        'main',
    )

    ordering = ('vehicle_name',)

class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
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
        'type',
        'available'
    )

    ordering = ('name',)


# Register your models here.
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleImages, VehicleImagesAdmin)
