from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from vehicles.models import Vehicle
from vehicles.views import unique_vehicle_parameters

# Create your views here.


def index(request):
    """
    Displays the home page
    """
    request.session["vehicle_bag"] = {}
    vehicle_makes = unique_vehicle_parameters.unique_vehicle_makes()
    vehicles = unique_vehicle_parameters.unique_vehicle_models()
    template = "home/index.html"
    context = {
        "static": settings.STATIC_URL,
        "vehicle_makes": vehicle_makes,
        "vehicles": vehicles,
    }
    return render(request, template, context)


def returns(request):
    """
    Displays the returns information page
    """
    template = "home/returns.html"

    return render(request, template)
