from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.db.models import Q
import requests
from .forms import VehicleForm


def add_vehicle(request):
    """ Add a new vhicle to the site"""
    form = VehicleForm()
    template = 'vehicles/add_vehicle.html'
    context = {
        'form': form,
    }
    return render(request, template, context)