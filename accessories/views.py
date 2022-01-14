from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from .models import Category, Accessory

# Create your views here.


def accessories(request):

    accessories = Accessory.objects.all()

    context = {
        'accessories': accessories,
        'media': settings.MEDIA_URL
    }
    template = 'accessories/accessories.html'

    return render(request, template, context)
