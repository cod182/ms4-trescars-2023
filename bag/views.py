from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.conf import settings
from django.db import models
from vehicles.models import unique_vehicle_parameters, Vehicle
from accessories.models import Accessory
from django.contrib import messages


# Create your views here.

def view_bag(request):
    """
    A view to return the bag content page
    """
    request.session['vehicle_bag'] = {}
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
    item = get_object_or_404(Accessory, pk=item_id)

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    messages.success(
            request, f'Added {item.brand.capitalize()} {item.accessory_type.capitalize()} to your bag.')

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified item to the specified amount"""

    accessory = get_object_or_404(Accessory, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f'Updated {accessory.brand.capitalize()} {accessory.accessory_type.capitalize()} quantity to { bag[item_id] }')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {accessory.brand.capitalize()} {accessory.accessory_type.capitalize()} from bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        accessory = get_object_or_404(Accessory, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {accessory.brand.capitalize()} {accessory.accessory_type.capitalize()} from bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item {e}')
        return HttpResponse(status=500)
