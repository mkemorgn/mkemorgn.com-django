from django.shortcuts import render

from mkemorgn_web.mkemorgn.models import AboutText, AboutPhoto


def index(request):
    return render(request, "index.html")


def about(request):
    about_text = AboutText.objects.all()
    about_photo = AboutPhoto.objects.all()
    return render(
        request,
        "about.html",
        {
            "about_text": about_text,
            "about_photo": about_photo,
        },
    )


def contact(request):
    return render(request, "contact.html")


def trips(request):
    return render(request, "trips.html")
