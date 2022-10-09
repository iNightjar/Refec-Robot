from django.shortcuts import render

import flights

from .models import Flight
# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights" : Flight.objects.all()
    })