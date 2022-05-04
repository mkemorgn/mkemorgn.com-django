from django.shortcuts import render

from mkemorgn_web.mkemorgn.models import (
    AboutText,
    AboutPhoto,
    TripsPhotos,
    DetroitPhotos,
)


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
    la = TripsPhotos.objects.get(name="LA")
    detroit = TripsPhotos.objects.get(name="Detroit")
    denver = TripsPhotos.objects.get(name="Denver")
    return render(
        request,
        "trips.html",
        {
            "la": la,
            "detroit": detroit,
            "denver": denver,
        },
    )


def detroit2020(request):
    detroit1 = DetroitPhotos.objects.get(name="detroit1")
    detroit2 = DetroitPhotos.objects.get(name="detroit2")
    detroit3 = DetroitPhotos.objects.get(name="detroit3")
    detroit4 = DetroitPhotos.objects.get(name="detroit4")
    detroit5 = DetroitPhotos.objects.get(name="detroit5")
    detroit6 = DetroitPhotos.objects.get(name="detroit6")
    detroit7 = DetroitPhotos.objects.get(name="detroit7")
    detroit8 = DetroitPhotos.objects.get(name="detroit8")
    detroit9 = DetroitPhotos.objects.get(name="detroit9")
    detroit10 = DetroitPhotos.objects.get(name="detroit10")
    detroit11 = DetroitPhotos.objects.get(name="detroit11")
    detroit12 = DetroitPhotos.objects.get(name="detroit12")
    detroit13 = DetroitPhotos.objects.get(name="detroit13")
    detroit14 = DetroitPhotos.objects.get(name="detroit14")
    return render(
        request,
        "detroit2020.html",
        {
            "detroit1": detroit1,
            "detroit2": detroit2,
            "detroit3": detroit3,
            "detroit4": detroit4,
            "detroit5": detroit5,
            "detroit6": detroit6,
            "detroit7": detroit7,
            "detroit8": detroit8,
            "detroit9": detroit9,
            "detroit10": detroit10,
            "detroit11": detroit11,
            "detroit12": detroit12,
            "detroit13": detroit13,
            "detroit14": detroit14,
        },
    )


def denver2020(request):
    return render(request, "denver2020.html")


def la2021(request):
    return render(request, "la2021.html")
