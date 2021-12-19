from django.shortcuts import render
from django.conf import settings
from .models import Vehicle

# Create your views here.

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
