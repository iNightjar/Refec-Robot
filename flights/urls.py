from operator import index
from unicodedata import name
from django.urls import path

from flights.models import Flight
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:flight_id>", views.flight,name="flight")
]