from django.shortcuts import render, redirect
from django.conf import settings
from django.db import models
from vehicles.models import unique_vehicle_parameters, Vehicle

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