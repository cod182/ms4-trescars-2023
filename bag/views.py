from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.conf import settings
from django.db import models
from vehicles.models import unique_vehicle_parameters, Vehicle
from django.contrib import messages


# Create your views here.

def view_bag(request):
    """
    A view to return the bag content page
    """

    template = 'bag/bag.html'
    context = {
        'static': settings.STATIC_URL,
    }
    return render(request, template, context)


def add_to_bag(request, item_id):
    """
    Add the specified item to the bag with quantity
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified item to the specified amount"""

    vehicle = get_object_or_404(Vehicle, sku=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    print(bag[item_id])
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated { vehicle.name } quantity to { bag[item_id] }')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed { vehicle.name } from bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Vehicle, sku=item_id)

        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed { product.name } from bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error remivng item {e}')
        return HttpResponse(status=500)