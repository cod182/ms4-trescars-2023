from django.urls import path
from .views import sendEmail

urlpatterns = [
    path("", sendEmail, name="sendEmail"),
    path("<item>", sendEmail, name="sendEmail"),
]
