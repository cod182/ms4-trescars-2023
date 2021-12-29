from django.shortcuts import render
from django.conf import settings
from django.db import models
from vehicles.models import unique_vehicle_parameters, Vehicle

# Create your views here.

def index(request):

    vehicle_makes = unique_vehicle_parameters.unique_vehicle_makes()
    vehicles = unique_vehicle_parameters.unique_vehicle_models()

    template = 'home/index.html'
    context = {
        'static': settings.STATIC_URL,
        'vehicle_makes': vehicle_makes,
        'vehicles': vehicles,
    }
    return render(request, template, context)
