from django.shortcuts import render
from django.conf import settings
from django.db import models
from vehicles.models import unique_vehicle_parameters, Vehicle

# Create your views here.

def view_bag(request):
    """
    A view to return the bag content page
    """
    vehicle_makes = unique_vehicle_parameters.unique_vehicle_makes()
    vehicles = unique_vehicle_parameters.unique_vehicle_models()

    template = 'bag/bag.html'

    return render(request, template)
