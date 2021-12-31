from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from vehicles.models import VehicleImages
from bag.contexts import bag_contents

import stripe

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    images = VehicleImages.objects.all()
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )

    if not bag:
        messages.error(request, "Bag is empty")
        return redirect(reverse('vehicles'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'media': settings.MEDIA_URL,
        'images': images,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,

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
