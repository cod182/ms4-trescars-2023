from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('reserve_vehicle_checkout/<vehicle>', views.reserve_vehicle_checkout, name='reserve_vehicle_checkout'),
    path('checkout_vehicle_success/<order_number>', views.checkout_vehicle_success, name='checkout_vehicle_success'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
