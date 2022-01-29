from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Category, Accessory


def handle_query_search(request):
    """
    takes the request and gets the query (q)
    searches the accessories
    """
    query = None

    query = request["q"]

    if not query:
        return None

    queries = (
        Q(name__icontains=query)
        | Q(description__icontains=query)
        | Q(vehicle_make__icontains=query)
        | Q(vehicle_model__icontains=query)
    )

    accessory_results = Accessory.objects.filter(queries)

    return accessory_results


def handleSorting(request, accessory_list):
    """
    takes the request and gets the sorting
    sorts the accessories by the sort key and direction
    """
    direction = None
    sortkey = None

    sortkey = request["sort"]
    if sortkey:
        accessories_results = accessory_list.order_by(sortkey)

    if "direction" in request:
        direction = request["direction"]
        if direction == "desc":
            sortkey = f"-{sortkey}"
        accessories_results = accessories_results.order_by(sortkey)

    return accessories_results


def accessories(request):
    """
    displayes the accessories category page
    """
    categories = Category.objects.all()

    context = {"categories": categories, "media": settings.MEDIA_URL}
    template = "accessories/accessories.html"

    return render(request, template, context)


def accessories_search(request):
    """
    displays the request category
    if no category returns to accessories
    gets all items with requested category
    """

    page_obj = None
    category = None

    if request.GET:
        accessory_results = Accessory.objects.all()

        if "category" in request.GET:
            category = request.GET["category"]
            categories = request.GET["category"].split(",")
            accessory_results = Accessory.objects.filter(
                category__name__in=categories)
        if "q" in request.GET:
            accessory_results = handle_query_search(request.GET)
            if not accessory_results:
                messages.error(request, "No Results or No Search Term Entered")
                return redirect(reverse("accessories"))

        if "sort" in request.GET:
            accessory_results = handleSorting(request.GET, accessory_results)

        paginator = Paginator(accessory_results, 24)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "accessories": page_obj,
            "media": settings.MEDIA_URL,
            "category": category,
        }

        template = "accessories/accessories_search.html"

        return render(request, template, context)
    return redirect(reverse("accessories"))


def accessory_detail(request, accessory_sku):
    """
    displays the requested accessory
    """
    accessory = Accessory.objects.get(sku=accessory_sku)

    template = "accessories/accessory_detail.html"

    context = {"accessory": accessory, "media": settings.MEDIA_URL}

    return render(request, template, context)
