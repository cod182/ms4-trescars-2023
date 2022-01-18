from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
from django.forms import inlineformset_factory
import requests
from vehicles.models import Vehicle, VehicleImages
from .forms import VehicleForm, VehicleImagesForm


@login_required
def management_home(request):
    template = "management/home.html"
    return render(request, template)


@login_required
def add_vehicle(request):
    """Add a new vhicle to the site"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only authorised users can do that!")
        return redirect(reverse("home"))

    if request.method == "POST":
        form_data = {
            "sku": request.POST["registration"].replace(" ", "").lower(),
            "name": request.POST["make"].lower()
            + "-"
            + request.POST["registration"].replace(" ", "").lower(),
            "registration": request.POST["registration"].lower(),
            "make": request.POST["make"].lower(),
            "model": request.POST["model"].lower(),
            "trim": request.POST["trim"].lower(),
            "colour": request.POST["colour"].lower(),
            "fuel": request.POST["fuel"].lower(),
            "engine_size": request.POST["engine_size"].lower(),
            "body_type": request.POST["body_type"].lower(),
            "gearbox": request.POST["gearbox"].lower(),
            "drivetrain": request.POST["drivetrain"].lower(),
            "seats": request.POST["seats"].lower(),
            "description": request.POST["description"].lower(),
            "price": 200,
            "full_price": request.POST["full_price"].lower(),
            "mileage": request.POST["mileage"].lower(),
            "model_year": request.POST["model_year"].lower(),
            "doors": request.POST["doors"].lower(),
            "type": "vehicle",
            "available": "yes",
        }
        form = VehicleForm(form_data)
        image_form = VehicleImagesForm(request.FILES)

        if form.is_valid():
            vehicle = form.save()

            image_number = 0
            mainImage = False
            for image in request.FILES.getlist("images"):

                if str(image) == str(request.POST["main"]):
                    mainImage = True

                image = VehicleImages.objects.create(
                    name=form_data["sku"] + "-" + str(image_number),
                    vehicle_name=Vehicle(vehicle.id),
                    image=image,
                    main=mainImage,
                )
                image_number += 1
                mainImage = False

            messages.success(request, "Sucsessfully added vehicle!")
            return redirect(reverse("vehicle_detail", args=[form_data["sku"]]))
        else:
            messages.error(
                request, "Failed to add vehicle. Please ensure the form is valid"
            )
    else:
        form = VehicleForm()
        image_form = VehicleImagesForm()

    template = "management/add_vehicle.html"
    context = {
        "form": form,
        "image_form": image_form,
    }
    return render(request, template, context)


@login_required
def update_vehicle(request, vehicle_sku):
    """Update an existing vehicle"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only authorised users can do that!")
        return redirect(reverse("home"))

    vehicle = Vehicle.objects.get(sku=vehicle_sku)

    if request.method == "POST":

        form_data = {
            "sku": request.POST["registration"].replace(" ", "").lower(),
            "name": request.POST["make"].lower()
            + "-"
            + request.POST["registration"].replace(" ", "").lower(),
            "registration": request.POST["registration"].lower(),
            "make": request.POST["make"].lower(),
            "model": request.POST["model"].lower(),
            "trim": request.POST["trim"].lower(),
            "colour": request.POST["colour"].lower(),
            "fuel": request.POST["fuel"].lower(),
            "engine_size": request.POST["engine_size"].lower(),
            "body_type": request.POST["body_type"].lower(),
            "gearbox": request.POST["gearbox"].lower(),
            "drivetrain": request.POST["drivetrain"].lower(),
            "seats": request.POST["seats"].lower(),
            "description": request.POST["description"].lower(),
            "price": 200,
            "full_price": request.POST["full_price"].lower(),
            "mileage": request.POST["mileage"].lower(),
            "model_year": request.POST["model_year"].lower(),
            "doors": request.POST["doors"].lower(),
            "type": "vehicle",
            "available": request.POST["available"],
        }
        form = VehicleForm(form_data, instance=vehicle)

        image_form = VehicleImagesForm(request.POST)
        x = request.POST.getlist("vehicle")
        print(x)

        if form.is_valid():
            vehicle = form.save()

            image_number = 0
            mainImage = False
            for image in request.POST.getlist("images"):

                if str(image) == str(request.POST["main"]):
                    mainImage = True

                image = VehicleImages.objects.create(
                    name=form_data["sku"] + "-" + str(image_number),
                    vehicle_name=Vehicle(vehicle.id),
                    image=image,
                    main=mainImage,
                )
                image_number += 1
                mainImage = False

            messages.success(request, "Sucsessfully updated vehicle!")
            return redirect(reverse("vehicle_detail", args=[form_data["sku"]]))
        else:
            messages.error(
                request, "Failed to add vehicle. Please ensure the form is valid"
            )
    else:

        LinkFormSet = inlineformset_factory(
            Vehicle,
            VehicleImages,
            extra=1,
            exclude=("name",),
        )

        messages.info(
            request,
            f"You are editing {vehicle.make.capitalize()} {vehicle.model.capitalize()} - {vehicle.registration.upper()}",
        )

        form = VehicleForm(instance=vehicle)
        image_form = LinkFormSet(instance=vehicle)

    template = "management/update_vehicle.html"
    context = {
        "form": form,
        "image_form": image_form,
        "vehicle": vehicle,
    }
    return render(request, template, context)


@login_required
def delete_vehicle(request, vehicle_sku):
    """delete vehicle from the database"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only authorised users can do that!")
        return redirect(reverse("home"))

    vehicle = get_object_or_404(Vehicle, sku=vehicle_sku)

    vehicle.delete()
    messages.success(request, "Vehicle deleted!")
    return redirect(reverse("vehicles"))


@login_required
def delete_vehicle_image(request, image_name):
    """delete a vehicle's image"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that!")
        return redirect(reverse("home"))

    image = get_object_or_404(VehicleImages, name=image_name)

    # image.delete()
    messages.success(request, "Image deleted!")

    return HttpResponse(status=200)
