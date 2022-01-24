from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator
from .models import Vehicle, VehicleImages
from django.db.models import Q
from decimal import Decimal
import requests
import json


class unique_vehicle_parameters:
    def unique_vehicle_makes():
        """
        Gets all the unique vehicle makes
        """
        vehicles = Vehicle.objects.filter(available="yes")
        vehicle_makes = []
        vehicle_makes.clear()

        for vehicle in vehicles:
            if vehicle.make not in vehicle_makes:
                vehicle_makes.append(vehicle.make)

        return vehicle_makes

    def unique_vehicle_models():
        """
        Gets the unique vehicle models with make
        """
        vehicles = Vehicle.objects.filter(available="yes")
        vehicle_models = []
        vehicle_models.clear()

        all_values = [value for elem in vehicle_models for value in elem.values()]

        for vehicle in vehicles:

            all_values = [value for elem in vehicle_models for value in elem.values()]
            if vehicle.model not in all_values:
                vehicle_models.append(
                    {"make": vehicle.make, "model": vehicle.model},
                )

        return vehicle_models

    def unique_vehicle_colours():
        """
        Gets all the unique vehicle colours
        """
        vehicles = Vehicle.objects.filter(available="yes")
        vehicle_colours = []
        vehicle_colours.clear()

        for vehicle in vehicles:
            if vehicle.colour not in vehicle_colours:
                vehicle_colours.append(vehicle.colour)

        return sorted(vehicle_colours)

    def unique_vehicle_engines():
        """
        Gets all the unique vehicle engines
        """
        vehicles = Vehicle.objects.filter(available="yes")
        vehicle_engines = []
        vehicle_engines.clear()

        for vehicle in vehicles:
            if vehicle.engine_size not in vehicle_engines:
                vehicle_engines.append(vehicle.engine_size)

        return sorted(vehicle_engines)

    def unique_vehicle_doors():
        """
        Gets all the unique vehicle doors
        """
        vehicles = Vehicle.objects.filter(available="yes")
        vehicle_doors = []
        vehicle_doors.clear()

        for vehicle in vehicles:
            if vehicle.doors not in vehicle_doors:
                vehicle_doors.append(vehicle.doors)

        return sorted(vehicle_doors)

    def unique_vehicle_body():
        """
        Gets all the unique vehicle body
        """
        vehicles = Vehicle.objects.filter(available="yes")
        vehicle_body = []
        vehicle_body.clear()

        for vehicle in vehicles:
            if vehicle.body_type not in vehicle_body:
                vehicle_body.append(vehicle.body_type)

        return sorted(vehicle_body)

    def unique_vehicle_fuels():
        """
        Gets all the unique vehicle fuels
        """
        vehicles = Vehicle.objects.filter(available="yes")
        vehicle_fuels = []
        vehicle_fuels.clear()

        for vehicle in vehicles:
            if vehicle.fuel not in vehicle_fuels:
                vehicle_fuels.append(vehicle.fuel)

        return sorted(vehicle_fuels)

    def unique_vehicle_drivetrains():
        """
        Gets all the unique vehicle drivetrains
        """
        vehicles = Vehicle.objects.filter(available="yes")
        vehicle_drivetrains = []
        vehicle_drivetrains.clear()

        for vehicle in vehicles:
            if vehicle.drivetrain not in vehicle_drivetrains:
                vehicle_drivetrains.append(vehicle.drivetrain)

        return sorted(vehicle_drivetrains)

    def unique_vehicle_years():
        """
        Gets all the unique vehicle year
        """
        vehicles = Vehicle.objects.filter(available="yes")
        vehicle_years = []
        vehicle_years.clear()

        for vehicle in vehicles:
            if vehicle.model_year not in vehicle_years:
                vehicle_years.append(vehicle.model_year)

        return sorted(vehicle_years)


def getRememberedSearchDict(request):
    remembered_search = {
        "make": request.GET["vehicle-make"],
        "model": request.GET["vehicle-model"],
        "year": request.GET["vehicle-model-year"],
        "price": request.GET["price-range"],
        "mileage": request.GET["mileage"],
        "colour": request.GET["vehicle-colour"],
        "engine": request.GET["vehicle-engine"],
        "doors": request.GET["vehicle-doors"],
        "body_type": request.GET["vehicle-body"],
        "fuel": request.GET["vehicle-fuel"],
        "drivetrain": request.GET["vehicle-drivetrain"],
    }
    return remembered_search


def vehicle_search(request):
    query_make = request.GET["vehicle-make"]
    query_model = request.GET["vehicle-model"]
    query_price = request.GET["price-range"]
    query_mileage = request.GET["mileage"]
    query_colour = request.GET["vehicle-colour"]
    query_engine = request.GET["vehicle-engine"]
    query_doors = request.GET["vehicle-doors"]
    query_body = request.GET["vehicle-body"]
    query_fuel = request.GET["vehicle-fuel"]
    query_drivetrain = request.GET["vehicle-drivetrain"]
    query_year = request.GET["vehicle-model-year"]

    if Decimal(query_engine) == 0:
        if int(query_price) == 30001:
            if int(query_mileage) == 100001:
                search = (
                    Q(make__icontains=query_make)
                    & Q(model__icontains=query_model)
                    & Q(price__gte=query_price)
                    & Q(mileage__gte=query_mileage)
                    & Q(colour__icontains=query_colour)
                    & Q(engine_size__gte + Decimal(query_engine))
                    & Q(doors__icontains=query_doors)
                    & Q(body_type__icontains=query_body)
                    & Q(fuel__icontains=query_fuel)
                    & Q(drivetrain__icontains=query_drivetrain)
                    & Q(model_year__icontains=query_year)
                )
            else:
                search = (
                    Q(make__icontains=query_make)
                    & Q(model__icontains=query_model)
                    & Q(price__gte=query_price)
                    & Q(mileage__lte=query_mileage)
                    & Q(colour__icontains=query_colour)
                    & Q(engine_size__gte=Decimal(query_engine))
                    & Q(doors__icontains=query_doors)
                    & Q(body_type__icontains=query_body)
                    & Q(fuel__icontains=query_fuel)
                    & Q(drivetrain__icontains=query_drivetrain)
                    & Q(model_year__icontains=query_year)
                )

        elif int(query_mileage) == 100001:
            if int(query_price) == 30001:
                search = (
                    Q(make__icontains=query_make)
                    & Q(model__icontains=query_model)
                    & Q(price__gte=query_price)
                    & Q(mileage__gte=query_mileage)
                    & Q(colour__icontains=query_colour)
                    & Q(engine_size__gte=Decimal(query_engine))
                    & Q(doors__icontains=query_doors)
                    & Q(body_type__icontains=query_body)
                    & Q(fuel__icontains=query_fuel)
                    & Q(drivetrain__icontains=query_drivetrain)
                    & Q(model_year__icontains=query_year)
                )
            else:
                search = (
                    Q(make__icontains=query_make)
                    & Q(model__icontains=query_model)
                    & Q(price__lte=query_price)
                    & Q(mileage__gte=query_mileage)
                    & Q(colour__icontains=query_colour)
                    & Q(engine_size__gte=Decimal(query_engine))
                    & Q(doors__icontains=query_doors)
                    & Q(body_type__icontains=query_body)
                    & Q(fuel__icontains=query_fuel)
                    & Q(drivetrain__icontains=query_drivetrain)
                    & Q(model_year__icontains=query_year)
                )
        else:
            search = (
                Q(make__icontains=query_make)
                & Q(model__icontains=query_model)
                & Q(price__lte=query_price)
                & Q(mileage__lte=query_mileage)
                & Q(colour__icontains=query_colour)
                & Q(engine_size__gte=Decimal(query_engine))
                & Q(doors__icontains=query_doors)
                & Q(body_type__icontains=query_body)
                & Q(fuel__icontains=query_fuel)
                & Q(drivetrain__icontains=query_drivetrain)
                & Q(model_year__icontains=query_year)
            )
    else:
        if int(query_price) == 30001:
            if int(query_mileage) == 100001:
                search = (
                    Q(make__icontains=query_make)
                    & Q(model__icontains=query_model)
                    & Q(price__gte=query_price)
                    & Q(mileage__gte=query_mileage)
                    & Q(colour__icontains=query_colour)
                    & Q(engine_size=Decimal(query_engine))
                    & Q(doors__icontains=query_doors)
                    & Q(body_type__icontains=query_body)
                    & Q(fuel__icontains=query_fuel)
                    & Q(drivetrain__icontains=query_drivetrain)
                    & Q(model_year__icontains=query_year)
                )
            else:
                search = (
                    Q(make__icontains=query_make)
                    & Q(model__icontains=query_model)
                    & Q(price__gte=query_price)
                    & Q(mileage__lte=query_mileage)
                    & Q(colour__icontains=query_colour)
                    & Q(engine_size=Decimal(query_engine))
                    & Q(doors__icontains=query_doors)
                    & Q(body_type__icontains=query_body)
                    & Q(fuel__icontains=query_fuel)
                    & Q(drivetrain__icontains=query_drivetrain)
                    & Q(model_year__icontains=query_year)
                )

        elif int(query_mileage) == 100001:
            if int(query_price) == 30001:
                search = (
                    Q(make__icontains=query_make)
                    & Q(model__icontains=query_model)
                    & Q(price__gte=query_price)
                    & Q(mileage__gte=query_mileage)
                    & Q(colour__icontains=query_colour)
                    & Q(engine_size=Decimal(query_engine))
                    & Q(doors__icontains=query_doors)
                    & Q(body_type__icontains=query_body)
                    & Q(fuel__icontains=query_fuel)
                    & Q(drivetrain__icontains=query_drivetrain)
                    & Q(model_year__icontains=query_year)
                )
            else:
                search = (
                    Q(make__icontains=query_make)
                    & Q(model__icontains=query_model)
                    & Q(price__lte=query_price)
                    & Q(mileage__gte=query_mileage)
                    & Q(colour__icontains=query_colour)
                    & Q(engine_size=Decimal(query_engine))
                    & Q(doors__icontains=query_doors)
                    & Q(body_type__icontains=query_body)
                    & Q(fuel__icontains=query_fuel)
                    & Q(drivetrain__icontains=query_drivetrain)
                    & Q(model_year__icontains=query_year)
                )
        else:
            search = (
                Q(make__icontains=query_make)
                & Q(model__icontains=query_model)
                & Q(price__lte=query_price)
                & Q(mileage__lte=query_mileage)
                & Q(colour__icontains=query_colour)
                & Q(engine_size=Decimal(query_engine))
                & Q(doors__icontains=query_doors)
                & Q(body_type__icontains=query_body)
                & Q(fuel__icontains=query_fuel)
                & Q(drivetrain__icontains=query_drivetrain)
                & Q(model_year__icontains=query_year)
            )

    return search


def handleSortBy(request, vehicles):
    """
    gets the sortkey from request
    gets the direction from request
    returns sorted list
    """
    sortkey = request.GET["sort"]
    sort = sortkey
    if sortkey == "pricex":
        sortkey = "full_price"
    elif sortkey == "age":
        sortkey = "model_year"
    vehicles = vehicles.order_by(sortkey)

    if "direction" in request.GET:
        direction = request.GET["direction"]
        if direction == "desc":
            sortkey = f"-{sortkey}"
        vehicles = vehicles.order_by(sortkey)

    current_sorting = f"{sort}_{direction}"

    return current_sorting, vehicles


def handleHomeVehicleSearch(request, vehicles):
    """
    takes the request from a home page search
    returns matching vehicles
    """
    query_make = request.GET["vehicle-make"]
    query_model = request.GET["vehicle-model"]

    if query_model:
        search = Q(make__icontains=query_make) & Q(model__icontains=query_model)
        vehicles = vehicles.filter(search)
    else:
        vehicles = vehicles.filter(Q(make__icontains=query_make))

    return vehicles


def request_info_from_dvla(reg):
    """[requests data from dvla on the requested vehicle form it's registration]

    Args:
        registration ([string]): [the registration fo the searched vehicle]

    Returns:
        [json]: [DVLA data on vehicle]
    """

    url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"

    payload = json.dumps(
        {
            "registrationNumber": reg,
        }
    )
    headers = {"x-api-key": settings.DVLA_API_KEY, "Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 404:
        print("Number Plate Not Found")

    return response.json


def all_vehicles(request):
    """
    A view to show all vehicles, including sorting
    and search queries
    """
    request.session["vehicle_bag"] = {}
    vehicles = Vehicle.objects.filter(available="yes")
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

    current_sorting = f"{sort}_{direction}"

    if request.GET:
        if "sort" in request.GET:
            current_sorting, vehicles = handleSortBy(request, vehicles)

        if "home-search" in request.GET:
            vehicles = handleHomeVehicleSearch(request, vehicles)

        if "vehicle-detailed-search" in request.GET:
            search = vehicle_search(request)
            vehicles = vehicles.filter(search)
            remembered_search = getRememberedSearchDict(request)

    paginator = Paginator(vehicles, 24)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "vehicles": page_obj,
        "images": images,
        "search_term": query,
        "current_sorting": current_sorting,
        "media": settings.MEDIA_URL,
        "vehicle_makes": vehicle_makes,
        "vehicle_models": vehicle_models,
        "vehicle_years": vehicle_years,
        "vehicle_colours": vehicle_colours,
        "vehicle_engines": vehicle_engines,
        "vehicle_doors": vehicle_doors,
        "vehicle_body": vehicle_body,
        "vehicle_fuels": vehicle_fuels,
        "vehicle_drivetrains": vehicle_drivetrains,
        "remembered_search": remembered_search,
    }
    return render(request, "vehicles/vehicles.html", context)


def vehicle_detail(request, vehicle_sku):
    """
    A view to show a vehicle detail page
    """
    request.session["vehicle_bag"] = {}
    vehicle = get_object_or_404(Vehicle, sku=vehicle_sku)

    images = VehicleImages.objects.filter(vehicle_name=vehicle.pk)

    dvla_data = request_info_from_dvla(reg=vehicle.registration)

    template = "vehicles/vehicle_detail.html"
    context = {
        "vehicle": vehicle,
        "images": images,
        "dvla_data": dvla_data,
        "media": settings.MEDIA_URL,
    }
    return render(request, template, context)
