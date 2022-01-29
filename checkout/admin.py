from django.contrib import admin
from .models import (
    Order,
    vehicle_order_line_item,
    accessory_order,
    accessory_order_line_item,
)


class vehicle_order_line_item_admin_inline(admin.TabularInline):
    model = vehicle_order_line_item
    readonly_fields = ("lineitem_total",)


class order_admin(admin.ModelAdmin):
    inlines = (vehicle_order_line_item_admin_inline,)

    readonly_fields = (
        "order_number",
        "order_type",
        "date",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "order_type",
        "status",
        "user_profile",
        "date",
        "full_name",
        "email",
        "phone_number",
        "country",
        "postcode",
        "town_or_city",
        "street_address1",
        "street_address2",
        "county",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "delivery_cost",
        "grand_total",
    )

    ordering = ("-date",)


class accessory_order_line_item_admin_inline(admin.TabularInline):
    model = accessory_order_line_item
    readonly_fields = ("lineitem_total",)


class accessory_order_admin(admin.ModelAdmin):
    inlines = (accessory_order_line_item_admin_inline,)

    readonly_fields = (
        "order_number",
        "order_type",
        "date",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "order_type",
        "user_profile",
        "date",
        "full_name",
        "email",
        "phone_number",
        "country",
        "postcode",
        "town_or_city",
        "street_address1",
        "street_address2",
        "county",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "delivery_cost",
        "grand_total",
    )

    ordering = ("-date",)


admin.site.register(Order, order_admin)
admin.site.register(accessory_order, accessory_order_admin)
