from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.accessories, name='accessories'),
    path('search/', views.accessories_search, name='accessories_search'),
    path('detail/<accessory_sku>', views.accessory_detail, name='accessory_detail'),
]
