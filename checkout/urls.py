from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_now/<item_id>', views.checkout_now, name='checkout_now'),
]
