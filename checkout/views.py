from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from vehicles.models import VehicleImages
# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    images = VehicleImages.objects.all()
    STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
    SECRET_KEY = settings.SECRET_KEY

    if not bag:
        messages.error(request, "Bag is empty")
        return redirect(reverse('vehicles'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'media': settings.MEDIA_URL,
        'images': images,
        'stripe_public_key':STRIPE_PUBLIC_KEY,
        'client_secret': SECRET_KEY,
    }

    return render(request, template, context)


def checkout_now(request, item_id):

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    images = VehicleImages.objects.all()
    STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
    SECRET_KEY = settings.SECRET_KEY

    if item_id in list(bag.keys()):
        messages.error(request, "Vehicle already in bag!")
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'media': settings.MEDIA_URL,
        'images': images,
        'stripe_public_key':STRIPE_PUBLIC_KEY,
        'client_secret': SECRET_KEY,
    }

    return render(request, template, context)
