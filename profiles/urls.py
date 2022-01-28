from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile, name="profile"),
    path(
        "order_detail/<order_number>",
        views.order_detail,
        name="order_detail"),
    path(
        "accessory_order_detail/<order_number>",
        views.accessory_order_detail,
        name="accessory_order_detail",
    ),
]
