from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import user_profile_form
from checkout.models import Order, accessory_order


@login_required
def profile(request):
    """Shows User Profile"""

    request.session["vehicle_bag"] = {}
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        if "delete-info" in request.POST:
            form = user_profile_form(request.POST, instance=user_profile)
            form.save()
        else:
            form = user_profile_form(request.POST, instance=user_profile)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile Updated")
            else:
                messages.error(request, "Please check the entered info.")

    form = user_profile_form(instance=user_profile)
    orders = user_profile.orders.all()
    accessory_orders = user_profile.AccessoryOrders.all()

    template = "profiles/profile.html"
    context = {
        "profile": user_profile,
        "form": form,
        "orders": orders,
        "accessory_orders": accessory_orders,
        "on_profile": True,
    }

    return render(request, template, context)


@login_required
def order_detail(request, order_number):

    user_profile = get_object_or_404(UserProfile, user=request.user)
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (f"This is a past order: {order_number}."))

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }
    return render(request, template, context)


@login_required
def accessory_order_detail(request, order_number):

    user_profile = get_object_or_404(UserProfile, user=request.user)
    order = get_object_or_404(accessory_order, order_number=order_number)

    messages.info(request, (f"This is a past order: {order_number}."))

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }
    return render(request, template, context)
