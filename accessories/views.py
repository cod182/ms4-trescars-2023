from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
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
    query = None
    sort = None
    direction = None

    if request.GET:
        accessories = Accessory.objects.all()

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            accessories = Accessory.objects.filter(category__name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a search term")
                return redirect(reverse('accessories'))
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(vehicle_make__icontains=query)  | Q(vehicle_model__icontains=query)
            accessories = Accessory.objects.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'price':
                sortkey = 'price'
                accessories = accessories.order_by(sortkey)

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                accessories = accessories.order_by(sortkey)

    paginator = Paginator(accessories, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'accessories': page_obj,
        'media': settings.MEDIA_URL
    }

    template = 'accessories/accessories_search.html'

    return render(request, template, context)
