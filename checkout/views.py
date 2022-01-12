from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from vehicles.models import Vehicle, VehicleImages
from bag.contexts import vehicle_bag_contents
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        if request.session.get('vehicle_bag'):
            stripe.PaymentIntent.modify(pid, metadata={
                'bag': json.dumps(request.session.get('vehicle_bag', {})),
                'save_info': request.POST.get('save_info'),
                'username': request.user,
                'order_type': 'vehicle',
            })
        else:
            stripe.PaymentIntent.modify(pid, metadata={
                'bag': json.dumps(request.session.get('accessory_bag', {})),
                'save_info': request.POST.get('save_info'),
                'username': request.user,
                'order_type': 'accessories',
            })

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def reserve_vehicle_checkout(request, vehicle):
    vehicle_bag = request.session.get('vehicle_bag', {})
    images = VehicleImages.objects.all()
    STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY
    STRIPE_SECRET_KEY = settings.STRIPE_SECRET_KEY

    # Auto fill save info
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'town_or_city': profile.default_town_or_city,
                'county': profile.default_county,
                'postcode': profile.default_postcode,
                'country': profile.default_country,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    if request.method == 'POST':
        if 'reserve_vehicle' in request.POST:

            vehicle_check = Vehicle.objects.get(sku=vehicle)

            if vehicle_check.available != 'yes':
                return redirect(reverse('vehicles'))
            else:

                if vehicle in list(vehicle_bag.keys()):
                    messages.error(request, "Vehicle already in bag!")

                else:
                    vehicle_bag[vehicle] = 1

                request.session['vehicle_bag'] = vehicle_bag

        else:
            vehicle_bag = request.session.get('vehicle_bag', {})

            form_data = {
                'order_type': request.POST['order_type'],
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'phone_number': request.POST['phone_number'],
                'postcode': request.POST['postcode'],
                'town_or_city': request.POST['town_or_city'],
                'street_address1': request.POST['street_address1'],
                'street_address2': request.POST['street_address2'],
                'county': request.POST['county'],
                'country': request.POST['country'],
            }

            order_form = OrderForm(form_data)
            if order_form.is_valid():
                order = order_form.save(commit=False)
                pid = request.POST.get('client_secret').split('_secret')[0]
                order.order_type = request.POST['order_type']
                order.stripe_pid = pid
                order.original_bag = json.dumps(vehicle_bag)
                order.save()
                for item_id, item_data in vehicle_bag.items():
                    try:
                        vehicle = Vehicle.objects.get(sku=item_id)
                        if isinstance(item_data, int):
                            order_line_item = OrderLineItem(
                                order=order,
                                vehicle=vehicle,
                            )
                            order_line_item.save()
                    except Vehicle.DoesNotExist:
                        messages.error(request, (
                            "One of the products in your bag wasn't found in our database."
                            "Please call us for assistance!")
                        )
                        order.delete()
                        return redirect(reverse('vehicles'))

                # Save the info to the user's profile
                request.session['save_info'] = 'save-info' in request.POST
                return redirect(reverse('checkout_vehicle_success', args=[order.order_number]))
            else:
                messages.error(request, 'There was an error with your form. \
                    Please double check your information.')

    current_bag = vehicle_bag_contents(request)
    total = current_bag['vehicle_grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )

    template = 'checkout/vehicle_checkout.html'

    context = {
        'order_form': order_form,
        'media': settings.MEDIA_URL,
        'images': images,
        'stripe_public_key': STRIPE_PUBLIC_KEY,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_vehicle_success(request, order_number):
    """
    Handle successful checkouts
    """
    vehicle_bag = request.session.get('vehicle_bag', {})
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'vehicle_bag' in request.session:
        for item in vehicle_bag:
            Vehicle.objects.filter(sku=item).update(available='no')
            del request.session['vehicle_bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


def checkout(request):
    images = VehicleImages.objects.all()
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    request.session['vehicle_bag'] = {}

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'default_country': request.POST['country'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    vehicle = Vehicle.objects.get(sku=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            vehicle=vehicle,
                        )
                        order_line_item.save()
                except Vehicle.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            # Save the info to the user's profile
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Bag is empty")
        return redirect(reverse('vehicles'))

    current_bag = vehicle_bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'media': settings.MEDIA_URL,
        'images': images,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    bag = request.session.get('bag', {})
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    order_type = request.POST.get('order_type')


    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        for item in bag:
            Vehicle.objects.filter(sku=item).update(available='')

        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
