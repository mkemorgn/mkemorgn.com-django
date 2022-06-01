from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("trips/", views.trips, name="trips"),
    path("trips/detroit2020", views.detroit2020, name="detroit2020"),
    path("trips/denver2020", views.denver2020, name="denver2020"),
    path("trips/la2021", views.la2021, name="la2021"),
]
