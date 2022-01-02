from django.http import HttpResponse

class StripeWH_Handler:
    """ Handles Stripe's Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handels generic unexpect event
        """
        return HttpResponse(
            content=f'Webhook Received: {event['type']}',
            status=200
        )
