from django.urls import path
from . import views

urlpatterns = [
    path("", views.management_home, name="management_home"),
    path("add_vehicle/", views.add_vehicle, name="add_vehicle"),
    path("update_vehicle/<vehicle_sku>", views.update_vehicle, name="update_vehicle"),
    path("delete_vehicle/<vehicle_sku>", views.delete_vehicle, name="delete_vehicle"),
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
    path("vehicle_orders/", views.vehicle_orders, name="vehicle_orders"),
    path("accessory_orders/", views.accessory_orders, name="accessory_orders"),
    path(
        "vehicle_order_update/<order_number>",
        views.vehicle_order_update,
        name="vehicle_order_update",
    ),
    path(
        "accessory_order_update/<order_number>",
        views.accessory_order_update,
        name="accessory_order_update",
    ),
]
