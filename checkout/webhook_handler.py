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
        print(event.data.object)
        return HttpResponse(
            content=f'Payment Succeeded: {event["type"]}',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle a payment intent failed webhook
        """
        return HttpResponse(
            content=f'Payment Failed: {event["type"]}',
            status=200)
