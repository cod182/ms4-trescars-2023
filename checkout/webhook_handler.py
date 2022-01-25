import json
import time
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from vehicles.models import Vehicle
from accessories.models import Accessory
from profiles.models import UserProfile
from .models import (
    Order,
    vehicle_order_line_item,
    accessory_order,
    accessory_order_line_item,
)


def save_user_info(profile):

    profile.default_phone_number = shipping_details.phone
    profile.default_country = shipping_details.address.country
    profile.default_postcode = shipping_details.address.postal_code
    profile.default_town_or_city = shipping_details.address.city
    profile.default_street_address1 = shipping_details.address.line1
    profile.default_street_address2 = shipping_details.address.line2
    profile.default_county = shipping_details.address.state
    profile.save()

    return profile


class StripeWH_Handler:
    """Handles Stripe's Webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """sends a email confirmation to customer on succsessful order"""
        customer_email = order.email
        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_email_subject.txt",
            {"order": order},
        )

        body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
        )
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [customer_email])

    def _send_company_alert_email(self, order):
        """Sends the company an alert about the order"""
        company_email = settings.DEFAULT_RECEIVING_EMAIL
        subject = render_to_string(
            "checkout/confirmation_emails/company_alert_subject.txt", {"order": order}
        )

        body = render_to_string(
            "checkout/confirmation_emails/company_alert_body.txt", {"order": order}
        )

        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [company_email])

    def handle_event(self, event):
        """
        Handle a unexpected webhook
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        order_type = intent.metadata.order_type
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile = save_user_info(username)

        order_exists = False
        attempt = 1

        if order_type == "vehicle":
            while attempt <= 5:
                try:
                    order = Order.objects.get(
                        order_type=order_type,
                        full_name__iexact=shipping_details.name,
                        email__iexact=billing_details.email,
                        phone_number__iexact=shipping_details.phone,
                        country__iexact=shipping_details.address.country,
                        postcode__iexact=shipping_details.address.postal_code,
                        town_or_city__iexact=shipping_details.address.city,
                        street_address1__iexact=shipping_details.address.line1,
                        street_address2__iexact=shipping_details.address.line2,
                        county__iexact=shipping_details.address.state,
                        grand_total=grand_total,
                        original_bag=bag,
                        stripe_pid=pid,
                    )
                    order_exists = True
                    break
                except Order.DoesNotExist:
                    attempt += 1
                    time.sleep(1)
        elif order_type == "accessories":
            while attempt <= 5:
                try:
                    order = accessory_order.objects.get(
                        order_type=order_type,
                        full_name__iexact=shipping_details.name,
                        email__iexact=billing_details.email,
                        phone_number__iexact=shipping_details.phone,
                        country__iexact=shipping_details.address.country,
                        postcode__iexact=shipping_details.address.postal_code,
                        town_or_city__iexact=shipping_details.address.city,
                        street_address1__iexact=shipping_details.address.line1,
                        street_address2__iexact=shipping_details.address.line2,
                        county__iexact=shipping_details.address.state,
                        grand_total=grand_total,
                        original_bag=bag,
                        stripe_pid=pid,
                    )
                    order_exists = True
                    break
                except accessory_order.DoesNotExist:
                    attempt += 1
                    time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            self._send_company_alert_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | Order already in database',
                status=200,
            )
        else:
            order = None
            if order_type == "vehicle":
                try:
                    order = Order.objects.create(
                        order_type=order_type,
                        full_name=shipping_details.name,
                        user_profile=profile,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.address.state,
                        original_bag=bag,
                        stripe_pid=pid,
                    )
                    for item_id, item_data in json.loads(bag).items():
                        if Vehicle.objects.get(sku=item_id):
                            order_items = Vehicle.objects.get(sku=item_id)

                            if isinstance(item_data, int):
                                order_line_item = vehicle_order_line_item(
                                    order=order,
                                    vehicle=order_items,
                                )
                            order_line_item.save()
                            Vehicle.objects.filter(sku=item_id).update(available="no")

                        else:
                            order_items = Accessory.objects.get(sku=item_id)

                            if isinstance(item_data, int):
                                order_line_item = vehicle_order_line_item(
                                    order=order,
                                    accessory=order_items,
                                    quantity=item_data,
                                )
                            order_line_item.save()

                except Exception as e:
                    if order:
                        order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500,
                    )
            elif order_type == "accessories":
                try:
                    order = accessory_order.objects.create(
                        order_type=order_type,
                        full_name=shipping_details.name,
                        user_profile=profile,
                        email=billing_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.address.state,
                        original_bag=bag,
                        stripe_pid=pid,
                    )
                    for item_id, item_data in json.loads(bag).items():
                        order_item = Accessory.objects.get(pk=item_id)

                        if isinstance(item_data, int):
                            order_line_item = accessory_order_line_item(
                                order=order,
                                accessory=order_item,
                                quantity=item_data,
                            )
                        order_line_item.save()
                        order_item.quantity_available -= 1
                        order_item.save()

                except Exception as e:
                    if order:
                        order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500,
                    )

        self._send_company_alert_email(order)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | Order created via webhook',
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle a payment intent failed webhook
        """
        return HttpResponse(content=f'Payment Failed: {event["type"]}', status=200)
