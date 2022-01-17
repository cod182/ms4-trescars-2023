from django.contrib import admin
from .models import Accessory, Category


class AccessoryAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'name',
        'brand',
        'vehicle_make',
        'vehicle_model',
        'price',
        'accessory_type',
        'quantity_available',
        'description',
        'image'
    )

    ordering = ('brand',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'image'
    )


admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(Category, CategoryAdmin)
