from django.contrib import admin
from .models import Vehicle, VehicleImages


class vehicle_images_admin(admin.ModelAdmin):
    list_display = (
        "name",
        "vehicle_name",
        "image",
        "main",
    )

    ordering = ("name",)


class images_inline(admin.StackedInline):
    model = VehicleImages


class vehicle_admin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "registration",
        "make",
        "model",
        "trim",
        "colour",
        "fuel",
        "engine_size",
        "body_type",
        "gearbox",
        "drivetrain",
        "seats",
        "description",
        "price",
        "full_price",
        "mileage",
        "model_year",
        "doors",
        "type",
        "available",
    )

    ordering = ("name",)

    inlines = [images_inline]


# Register your models here.
admin.site.register(Vehicle, vehicle_admin)
admin.site.register(VehicleImages, vehicle_images_admin)
