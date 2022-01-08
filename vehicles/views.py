from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator
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
    request.session['vehicle_bag'] = {}
    vehicles = Vehicle.objects.filter(available='yes')
    images = VehicleImages.objects.all()
    query = None
    sort = None
    direction = None
    remembered_search = None

    vehicle_makes = unique_vehicle_parameters.unique_vehicle_makes()
    vehicle_models = unique_vehicle_parameters.unique_vehicle_models()
    vehicle_colours = unique_vehicle_parameters.unique_vehicle_colours()
    vehicle_doors = unique_vehicle_parameters.unique_vehicle_doors()
    vehicle_body = unique_vehicle_parameters.unique_vehicle_body()
    vehicle_fuels = unique_vehicle_parameters.unique_vehicle_fuels()
    vehicle_engines = unique_vehicle_parameters.unique_vehicle_engines()
    vehicle_drivetrains = unique_vehicle_parameters.unique_vehicle_drivetrains()
    vehicle_years = unique_vehicle_parameters.unique_vehicle_years()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'pricex':
                sortkey = 'full_price'
                vehicles = vehicles.order_by(sortkey)

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            vehicles = vehicles.order_by(sortkey)

        if 'home-search' in request.GET:
            query_make = request.GET['vehicle-make']
            query_model = request.GET['vehicle-model']

            if query_model:
                search = Q(
                    make__icontains=query_make) & Q(
                        model__icontains=query_model)

                vehicles = vehicles.filter(search)
            else:
                vehicles = vehicles.filter(Q(make__icontains=query_make))

        if 'vehicle-detailed-search' in request.GET:

            query_make = request.GET['vehicle-make']
            query_model = request.GET['vehicle-model']
            query_price = request.GET['price-range']
            query_mileage = request.GET['mileage']
            query_colour = request.GET['vehicle-colour']
            query_engine = request.GET['vehicle-engine']
            query_doors = request.GET['vehicle-doors']
            query_body = request.GET['vehicle-body']
            query_fuel = request.GET['vehicle-fuel']
            query_drivetrain = request.GET['vehicle-drivetrain']
            query_year = request.GET['vehicle-model-year']

            if int(query_price) == 30001:
                if int(query_mileage) == 100001:
                    search = Q(make__icontains=query_make) & Q(model__icontains=query_model) & Q(price__gte=query_price) & Q(mileage__gte=query_mileage) & Q(colour__icontains=query_colour) & Q(engine_size__icontains=query_engine) & Q(doors__icontains=query_doors) & Q(body_type__icontains=query_body) & Q(fuel__icontains=query_fuel) & Q(drivetrain__icontains=query_drivetrain) & Q(model_year__icontains=query_year)
                else:
                    search = Q(make__icontains=query_make) & Q(model__icontains=query_model) & Q(price__gte=query_price) & Q(mileage__lte=query_mileage) & Q(colour__icontains=query_colour) & Q(engine_size__icontains=query_engine) & Q(doors__icontains=query_doors) & Q(body_type__icontains=query_body) & Q(fuel__icontains=query_fuel) & Q(drivetrain__icontains=query_drivetrain) & Q(model_year__icontains=query_year)

            elif int(query_mileage) == 100001:
                if int(query_price) == 30001:
                    search = Q(make__icontains=query_make) & Q(model__icontains=query_model) & Q(price__gte=query_price) & Q(mileage__gte=query_mileage) & Q(colour__icontains=query_colour) & Q(engine_size__icontains=query_engine) & Q(doors__icontains=query_doors) & Q(body_type__icontains=query_body) & Q(fuel__icontains=query_fuel) & Q(drivetrain__icontains=query_drivetrain) & Q(model_year__icontains=query_year)
                else:
                    search = Q(make__icontains=query_make) & Q(model__icontains=query_model) & Q(price__lte=query_price) & Q(mileage__gte=query_mileage) & Q(colour__icontains=query_colour) & Q(engine_size__icontains=query_engine) & Q(doors__icontains=query_doors) & Q(body_type__icontains=query_body) & Q(fuel__icontains=query_fuel) & Q(drivetrain__icontains=query_drivetrain) & Q(model_year__icontains=query_year)
            else:
                search = Q(make__icontains=query_make) & Q(model__icontains=query_model) & Q(price__lte=query_price) & Q(mileage__lte=query_mileage) & Q(colour__icontains=query_colour) & Q(engine_size__icontains=query_engine) & Q(doors__icontains=query_doors) & Q(body_type__icontains=query_body) & Q(fuel__icontains=query_fuel) & Q(drivetrain__icontains=query_drivetrain) & Q(model_year__icontains=query_year)

            vehicles = vehicles.filter(search)



            remembered_search = {
                'make': query_make,
                'model': query_model,
                'year': query_year,
                'price': query_price,
                'mileage': query_mileage,
                'colour': query_colour,
                'engine': query_engine,
                'doors': query_doors,
                'body_type': query_body,
                'fuel': query_fuel,
                'drivetrain': query_drivetrain,
            }

    current_sorting = f'{sort}_{direction}'

    paginator = Paginator(vehicles, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'vehicles': page_obj,
        'images': images,
        'search_term': query,
        'current_sorting': current_sorting,
        'media': settings.MEDIA_URL,
        'vehicle_makes': vehicle_makes,
        'vehicle_models':  vehicle_models,
        'vehicle_years': vehicle_years,
        'vehicle_colours': vehicle_colours,
        'vehicle_engines': vehicle_engines,
        'vehicle_doors': vehicle_doors,
        'vehicle_body': vehicle_body,
        'vehicle_fuels': vehicle_fuels,
        'vehicle_drivetrains': vehicle_drivetrains,
        'remembered_search': remembered_search
    }
    return render(request, 'vehicles/vehicles.html', context)


def vehicle_detail(request, vehicle_sku):
    """
    A view to show a vehicle detail page
    """
    request.session['vehicle_bag'] = {}
    vehicle = get_object_or_404(Vehicle, sku=vehicle_sku)

    images = VehicleImages.objects.filter(vehicle_name=vehicle.pk)

    dvla_data = request_info_from_dvla(reg=vehicle.registration)

    context = {
        'vehicle': vehicle,
        'images': images,
        'dvla_data': dvla_data,
        'media': settings.MEDIA_URL,
    }
    return render(request, 'vehicles/vehicle_detail.html', context)
