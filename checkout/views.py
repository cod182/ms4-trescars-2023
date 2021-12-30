from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from vehicles.models import VehicleImages
# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    images = VehicleImages.objects.all()
    if not bag:
        messages.error(request, "Bag is empty")
        return redirect(reverse('vehicles'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'media': settings.MEDIA_URL,
        'images': images
    }

    return render(request, template, context)
