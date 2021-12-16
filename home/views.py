from django.shortcuts import render
from django.conf import settings

# Create your views here.

def index(request):
    template = 'home/index.html'
    context = {
        'static': settings.STATIC_URL,
    }
    return render(request, template, context)