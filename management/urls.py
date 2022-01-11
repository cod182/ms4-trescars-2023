from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.management_home, name='management_home'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('update_vehicle/', views.update_vehicle, name='update_vehicle'),
]
