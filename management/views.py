from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
from django.forms import inlineformset_factory
import requests
import datetime
from vehicles.models import Vehicle, VehicleImages
from accessories.models import Accessory
from .forms import vehicle_form, vehicle_images_form, accessory_form


def handle_delete_images(request):
    """
    -takes request.post, get any vehicleimages refrences and puts them in
    a list.
    - iterates list for 'DELETE'
    - get's string from delete and iterates for id. get's id
    - submits id to VehicelImages to get image
    - deletes image
    """
    p_list = dict()

    for x in request:
        if "vehicleimages" in x:
            if request[x] != "":
                p_list[x] = request[x]

    image_id = None
    id_key = ""
    p = ""

    for key, value in p_list.items():

        if "DELETE" in key:

            p = key.split("-DELETE")[0]
            id_key = p + "-id"

            for k, v in p_list.items():
                if id_key in k:
                    image_id = v
                    print("image id", image_id)
                    obj = VehicleImages.objects.get(pk=image_id)
                    obj.delete()

                    image_id = None


def handle_main_image_checked(request):
    """
    -takes request.post, get any vehicleimages refrneces and put them in
    a list.
    - iterates list for 'main', sets it true.
    - get's string from main and iterates for id. get's id
    - submites id to VehicelImages to get image
    - set's main to true and saves
    - if main doesn't exist with id, gets image and sets main false
    """
    p_list = dict()

    for x in request:
        if "vehicleimages" in x:
            if request[x] != "":
                p_list[x] = request[x]

    image_id = None
    main = False
    id_key = ""
    p = ""

    for key, value in p_list.items():

        if "main" in key:
            main = True

            p = key.split("-main")[0]
            id_key = p + "-id"

            for k, v in p_list.items():
                if id_key in k:
                    image_id = v

                    obj = VehicleImages.objects.get(pk=image_id)
                    obj.main = main
                    obj.save()

                    image_id = None
                    main = False

        if key != id_key:
            if "id" in key:
                main = False
                imgId = value
                obj = VehicleImages.objects.get(pk=imgId)
                obj.main = main
                obj.save()

                imgId = None


def handle_images_upload(requestFiles, requestPost, form_data, vehicle, FROM):
    """
    Gets the images from Post adds them to the table
    if main in in request, main is added to image
    """
    image_number = 0
    mainImage = False
    for image in requestFiles.getlist("images"):
        if FROM == "new_vehicle":
            if str(image) == str(requestPost["main"]):
                mainImage = True

        image = VehicleImages.objects.create(
            name=form_data["sku"] + "-" + str(image_number),
            vehicle_name=Vehicle(vehicle.id),
            image=image,
            main=mainImage,
        )
        image_number += 1
        mainImage = False


def handle_delete_accessory_image(accessory_id):
    """
    Takes in the accessory_id. Finds the accessory and delets the images
    """
    accessory = Accessory.objects.get(pk=accessory_id)
    accessory.image.delete()
    accessory.save()


def get_form_data(request):
    """
    Gets the form data in a dictionary and returns it
    """
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
    return form_data


def check_if_vehicle_in_database(request):
    """
    Check if the vehicle is already in the database via the sku
    """
    sku = request.POST["registration"].replace(" ", "").lower()
    vehicle = Vehicle.objects.filter(sku=sku)
    if len(vehicle) >= 1:
        return True
    return False


def get_form_update_data(request):
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
        "full_price": request.POST["full_price"].lower(),
        "mileage": request.POST["mileage"].lower(),
        "model_year": request.POST["model_year"].lower(),
        "doors": request.POST["doors"].lower(),
        "available": request.POST["available"],
    }
    return form_data


def get_accessory_form_data(request):
    form_data = {
        "category": request.POST["category"].lower(),
        "sku": request.POST["brand"].replace(" ", "-").lower()
        + "-"
        + request.POST["accessory_type"].replace(" ", "-").lower()
        + "-"
        + request.POST["vehicle_model"].replace(" ", "-").lower()
        + "-"
        + str(datetime.datetime.now().year),
        "name": request.POST["brand"].lower()
        + "-"
        + request.POST["accessory_type"].lower(),
        "brand": request.POST["brand"].lower(),
        "vehicle_make": request.POST["vehicle_make"].lower(),
        "vehicle_model": request.POST["vehicle_model"].lower(),
        "price": request.POST["price"].lower(),
        "quantity_available": request.POST["quantity_available"].lower(),
        "accessory_type": request.POST["accessory_type"].lower(),
        "description": request.POST["description"].lower(),
    }
    return form_data


@login_required
def management_home(request):
    """
    retuns the management page
    """
    template = "management/home.html"
    return render(request, template)


@login_required
def add_vehicle(request):
    """Add a new vhicle to the site"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only authorised users can do that!")
        return redirect(reverse("management_home"))

    if request.method == "POST":
        form_data = get_form_data(request)
        check = check_if_vehicle_in_database(request)
        if check:
            messages.error(request, "Vehicle already in Database")
            return redirect(reverse("add_vehicle"))
        form = vehicle_form(form_data)
        image_form = vehicle_images_form(request.FILES)

        if form.is_valid():
            vehicle = form.save()

            handle_images_upload(
                request.FILES, request.POST, form_data, vehicle, "new_vehicle"
            )

            messages.success(request, "Sucsessfully added vehicle!")
            return redirect(reverse("vehicle_detail", args=[form_data["sku"]]))
        else:
            messages.error(
                request, "Failed to add vehicle. Please ensure the form is valid"
            )
    else:
        form = vehicle_form()
        image_form = vehicle_images_form()

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
        return redirect(reverse("management_home"))

    vehicle = get_object_or_404(Vehicle, sku=vehicle_sku)

    if request.method == "POST":
        form_data = get_form_update_data(request)
        form = vehicle_form(form_data, instance=vehicle)
        more_images_form = vehicle_images_form(request.FILES)

        if form.is_valid():
            vehicle = form.save()

            handle_main_image_checked(request.POST)
            handle_delete_images(request.POST)
            handle_images_upload(
                request.FILES, request.POST, form_data, vehicle, "update_vehicle"
            )

            messages.success(request, "Sucsessfully updated vehicle!")
            return redirect(reverse("vehicle_detail", args=[form_data["sku"]]))
        else:
            messages.error(
                request, "Failed to add vehicle. Please ensure the form is valid"
            )

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

    form = vehicle_form(instance=vehicle)
    image_form = LinkFormSet(instance=vehicle)
    more_images_form = vehicle_images_form(request.FILES)

    template = "management/update_vehicle.html"
    context = {
        "form": form,
        "image_form": image_form,
        "more_images_form": more_images_form,
        "vehicle": vehicle,
    }
    return render(request, template, context)


@login_required
def delete_vehicle(request, vehicle_sku):
    """delete vehicle from the database"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only authorised users can do that!")
        return redirect(reverse("management_home"))

    vehicle = get_object_or_404(Vehicle, sku=vehicle_sku)

    vehicle.delete()

    messages.success(request, "Vehicle deleted!")
    return redirect(reverse("vehicles"))


@login_required
def add_accessory(request):
    """Add a new accessory to the site"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only authorised users can do that!")
        return redirect(reverse("home"))

    if request.method == "POST":
        form_data = get_accessory_form_data(request)

        form = accessory_form(form_data, request.FILES)
        if form.is_valid():
            messages.success(request, "Sucsessfully added product!")
            return redirect(reverse("accessory_detail", args=[form_data["sku"]]))
        else:
            messages.error(
                request, "Failed to add accessory. Please ensure the form is valid"
            )
    else:
        form = accessory_form

    template = "management/add_accessory.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def update_accessory(request, accessory_id):
    """Update a accessory on the site"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that!")
        return redirect(reverse("management_home"))

    accessory = get_object_or_404(Accessory, pk=accessory_id)

    if request.method == "POST":
        form_data = get_accessory_form_data(request)
        form = accessory_form(form_data, request.FILES, instance=accessory)

        if form.is_valid():
            form.save()
            if "image-clear" in request.POST:
                handle_delete_accessory_image(accessory_id)

            messages.success(
                request,
                "Updated Successfully",
            )
            return redirect(reverse("accessory_detail", args=[accessory.sku]))
        else:
            messages.error(
                request, "Failed to update accessory.  Please ensure form is valid"
            )
    form = accessory_form(instance=accessory)
    messages.info(request, f"You are editing {accessory.name}")

    template = "management/update_accessory.html"
    context = {
        "form": form,
        "accessory": accessory,
    }

    return render(request, template, context)


@login_required
def delete_accessory(request, accessory_id):
    """delete accessory from the database"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only authorised users can do that!")
        return redirect(reverse("management_home"))

    accessory = get_object_or_404(Accessory, pk=accessory_id)

    accessory.delete()
    messages.success(request, "Accessory deleted!")

    return redirect(reverse("accessories"))
