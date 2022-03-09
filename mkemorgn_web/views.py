from django.shortcuts import render

from mkemorgn_web.mkemorgn.models import About


def index(request):
    return render(request, "index.html")


def about(request):
    about_page = About.objects.all()
    return render(request, "about.html", {"about_page": about_page})


def contact(request):
    return render(request, "contact.html")


def trips(request):
    return render(request, "trips.html")
