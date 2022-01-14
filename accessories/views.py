from django.shortcuts import render, get_object_or_404, redirect, reverse

# Create your views here.


def accessories(request):
    template = 'accessories/accessories.html'

    return render(request, template)
