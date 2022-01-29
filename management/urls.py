from django.urls import path
from . import views

urlpatterns = [
    path("", views.management_home, name="management_home"),
    path("add_vehicle/", views.add_vehicle, name="add_vehicle"),
    path(
        "update_vehicle/<vehicle_sku>",
        views.update_vehicle,
        name="update_vehicle"),
    path(
        "delete_vehicle/<vehicle_sku>",
        views.delete_vehicle,
        name="delete_vehicle"),
    path("add_accessory/", views.add_accessory, name="add_accessory"),
    path(
        "update_accessory/<int:accessory_id>",
        views.update_accessory,
        name="update_accessory",
    ),
    path(
        "delete_accessory/<int:accessory_id>",
        views.delete_accessory,
        name="delete_accessory",
    ),
    path("orders/",
         views.view_orders,
         name="orders")
]
