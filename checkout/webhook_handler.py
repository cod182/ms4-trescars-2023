from django.http import HttpResponse

class StripeWH_Handler:
    """ Handles Stripe's Webhooks """

    def __init__(self, request):
        self.request = request


    def handle_event(self, event):
        """
        Handle a unexpected webhook
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle a payment intent succeeded webhook
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)


    def handle_payment_intent_failed(self, event):
        """
        Handle a payment intent failed webhook
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)