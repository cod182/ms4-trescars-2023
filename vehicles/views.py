from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .models import Vehicle, VehicleImages, unique_vehicle_parameters
from django.db.models import Q
import requests
import json


def request_info_from_dvla(reg):
    """[requests data from dvla on the requested vehicle form it's registration]

    Args:
        registration ([string]): [the registration fo the searched vehicle]

    Returns:
        [json]: [DVLA data on vehicle]
    """

    url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

    payload = json.dumps({
        "registrationNumber": reg,
        })
    headers = {
        'x-api-key': settings.DVLA_API_KEY,
        'Content-Type': 'application/json'
        }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json


def all_vehicles(request):
    """
    A view to show all vehicles, including sorting
    and search queries
    """
    vehicles = Vehicle.objects.all()
    query = None
    sort = None
    direction = None

    vehicle_makes = unique_vehicle_parameters.unique_vehicle_makes()

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

        if 'home-search' in request.GET:
            query_make = request.GET['vehicle-make']
            query_model = request.GET['vehicle-model']

            if len(query_model) < 1:
                vehicles = vehicles.filter(Q(make__icontains=query_make))
            else:
                vehicles_make = vehicles.filter(Q(
                    make__icontains=query_make.lower()))
                vehicles = vehicles_make.filter(Q(
                    model=query_model.lower()))


    current_sorting = f'{sort}_{direction}'

    context = {
        'vehicles': vehicles,
        'search_term': query,
        'current_sorting': current_sorting,
        'static': settings.STATIC_URL,
        'media': settings.MEDIA_URL,
        'vehicle_makes': vehicle_makes,
    }
    return render(request, 'vehicles/vehicles.html', context)


def vehicle_detail(request, vehicle_sku):
    """
    A view to show a vehicle detail page
    """
    vehicle = get_object_or_404(Vehicle, sku=vehicle_sku)

    images = VehicleImages.objects.filter(vehicle_name=vehicle.pk)

    dvla_data = request_info_from_dvla(reg=vehicle.registration)

    # original_date = datetime.strptime(dvla_data.get('motExpiryDate'), '%Y-%m-%d')
    # formatted_date = original_date.strftime("%d:%m:%Y")
    # print(formatted_date)

    context = {
        'vehicle': vehicle,
        'images': images,
        'dvla_data': dvla_data,
        'static': settings.STATIC_URL,
        'media': settings.MEDIA_URL,
    }
    return render(request, 'vehicles/vehicle_detail.html', context)
