from django.contrib import admin
from .models import Accessory, Category


class AccessoryAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'name',
        'brand',
        'vehicle_make',
        'vehicle_mode',
        'price',
        'accessory_type',
        'quantity_available',
        'description',
        'image'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )



admin.site.register(Accessory, AccessoryAdmin)
admin.site.register(Category, CategoryAdmin)
