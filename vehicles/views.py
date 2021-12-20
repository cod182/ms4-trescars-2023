from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from .models import Vehicle, VehicleImages
import requests
import json


def request_info_from_dvla(registration):
    """[requests data from dvla on the requested vehicle form it's registration]

    Args:
        registration ([string]): [the registration fo the searched vehicle]

    Returns:
        [json]: [DVLA data on vehicle]
    """

url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

payload = json.dumps({
  "registrationNumber": registration
})
headers = {
  'x-api-key': settings.DVLA_API,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


def all_vehicles(request):
    """
    A view to show all vehicles, including sorting
    and search queries
    """
    vehicles = Vehicle.objects.all()
    query = None
    sort = None
    direction = None
    vehicle_makes = []
    vehicle_models = []

    vehicle_makes.clear()
    for vehicle in vehicles:
        if vehicle.make not in vehicle_makes:
            vehicle_makes.append(vehicle.make)

        if vehicle.model not in vehicle_models:
            vehicle_models.append(vehicle.model)

    vehicle_makes.sort()
    vehicle_models.sort()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'make':
                sortkey == 'lower_name'
                vehicles = vehicles.annotate(lower_name=Lower('make'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            vehicles = vehicles.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a search term")
                return redirect(reverse('vehicles'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'vehicles': vehicles,
        'search_term': query,
        'current_sorting': current_sorting,
        'static': settings.STATIC_URL,
        'media': settings.MEDIA_URL,
        'vehicle_makes': vehicle_makes,
        'vehicle_models': vehicle_models
    }
    return render(request, 'vehicles/vehicles.html', context)


def vehicle_detail(request, vehicle_sku):
    """
    A view to show a vehicle detail page
    """
    vehicle = get_object_or_404(Vehicle, sku=vehicle_sku)

    images = VehicleImages.objects.filter(vehicle_name=vehicle.pk)

    dvla_data = request_info_from_dvla(vehicle.registration)

    context = {
        'vehicle': vehicle,
        'images': images,
        'dvla_data': dvla_data,
        'static': settings.STATIC_URL,
        'media': settings.MEDIA_URL,
    }
    return render(request, 'vehicles/vehicle_detail.html', context)
