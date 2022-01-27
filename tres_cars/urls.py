from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("home.urls")),
    path("vehicles/", include("vehicles.urls")),
    path("accessories/", include("accessories.urls")),
    path("bag/", include("bag.urls")),
    path("checkout/", include("checkout.urls")),
    path("profile/", include("profiles.urls")),
    path("management/", include("management.urls")),
    path("send_email/", include("mailer.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
