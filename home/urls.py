from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("returns", views.returns_page, name="returns_page"),
]
