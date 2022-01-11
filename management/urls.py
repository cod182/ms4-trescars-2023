from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.management_home, name='management_home'),
    path('vehicles/', views.manage_vehicles, name='manage_vehicles'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
]
