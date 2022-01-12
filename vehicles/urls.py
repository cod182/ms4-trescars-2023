from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.all_vehicles, name='vehicles'),
    path('<vehicle_sku>/', views.vehicle_detail, name='vehicle_detail'),
]
