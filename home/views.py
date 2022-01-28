from django.shortcuts import render
from django.conf import settings
from vehicles.views import unique_vehicle_params

# Create your views here.


def index(request):
    """
    Displays the home page
    """
    request.session["vehicle_bag"] = {}
    vehicle_makes = unique_vehicle_params.unique_vehicle_makes()
    vehicles = unique_vehicle_params.unique_vehicle_models()
    template = "home/index.html"
    context = {
        "static": settings.STATIC_URL,
        "vehicle_makes": vehicle_makes,
        "vehicles": vehicles,
    }
    return render(request, template, context)


def returns_page(request):
    """
    Displays the returns information page
    """
    template = "home/returns-page.html"

    return render(request, template)
