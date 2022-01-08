from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
]
