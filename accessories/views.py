from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.db.models import Q
from .models import Category, Accessory

# Create your views here.


def accessories(request):

    accessories = Accessory.objects.all()
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'media': settings.MEDIA_URL
    }
    template = 'accessories/accessories.html'

    return render(request, template, context)


def accessories_search(request):

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            accessories = Accessory.objects.filter(category__name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a search term")
                return redirect(reverse('accessories'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            accessories = Accessory.objects.filter(queries)

    context = {
        'accessories': accessories,
    }

    template = 'accessories/accessories_search.html'

    return render(request, template, context)
