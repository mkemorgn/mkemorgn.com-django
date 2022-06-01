from django.shortcuts import render

from mkemorgn_web.mkemorgn.models import (
    IndexPhotos,
    AboutPhoto,
    TripsPhotos,
    Detroit2020Photos,
    Denver2020Photos,
    LA2021Photos,
)


def index(request):
    one = IndexPhotos.objects.get(name="1")
    two = IndexPhotos.objects.get(name="2")
    three = IndexPhotos.objects.get(name="3")
    four = IndexPhotos.objects.get(name="4")
    five = IndexPhotos.objects.get(name="5")
    six = IndexPhotos.objects.get(name="6")
    seven = IndexPhotos.objects.get(name="7")
    eight = IndexPhotos.objects.get(name="8")
    return render(
        request,
        "index.html",
        {
            "one": one,
            "two": two,
            "three": three,
            "four": four,
            "five": five,
            "six": six,
            "seven": seven,
            "eight": eight,
        },
    )


def about(request):
    about_photo = AboutPhoto.objects.all()
    return render(
        request,
        "about.html",
        {
            "about_photo": about_photo,
        },
    )


def trips(request):
    la2021 = TripsPhotos.objects.get(name="la2021")
    detroit2020 = TripsPhotos.objects.get(name="detroit2020")
    denver2020 = TripsPhotos.objects.get(name="denver2020")
    return render(
        request,
        "trips.html",
        {
            "la2021": la2021,
            "detroit2020": detroit2020,
            "denver2020": denver2020,
        },
    )


def detroit2020(request):
    detroit1 = Detroit2020Photos.objects.get(name="detroit1")
    detroit2 = Detroit2020Photos.objects.get(name="detroit2")
    detroit3 = Detroit2020Photos.objects.get(name="detroit3")
    detroit4 = Detroit2020Photos.objects.get(name="detroit4")
    detroit5 = Detroit2020Photos.objects.get(name="detroit5")
    detroit6 = Detroit2020Photos.objects.get(name="detroit6")
    detroit7 = Detroit2020Photos.objects.get(name="detroit7")
    detroit8 = Detroit2020Photos.objects.get(name="detroit8")
    detroit9 = Detroit2020Photos.objects.get(name="detroit9")
    detroit10 = Detroit2020Photos.objects.get(name="detroit10")
    detroit11 = Detroit2020Photos.objects.get(name="detroit11")
    detroit12 = Detroit2020Photos.objects.get(name="detroit12")
    detroit13 = Detroit2020Photos.objects.get(name="detroit13")
    detroit14 = Detroit2020Photos.objects.get(name="detroit14")
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
    denver1 = Denver2020Photos.objects.get(name="denver1")
    denver2 = Denver2020Photos.objects.get(name="denver2")
    denver3 = Denver2020Photos.objects.get(name="denver3")
    denver4 = Denver2020Photos.objects.get(name="denver4")
    denver5 = Denver2020Photos.objects.get(name="denver5")
    denver6 = Denver2020Photos.objects.get(name="denver6")
    denver7 = Denver2020Photos.objects.get(name="denver7")
    denver8 = Denver2020Photos.objects.get(name="denver8")
    denver9 = Denver2020Photos.objects.get(name="denver9")
    denver10 = Denver2020Photos.objects.get(name="denver10")
    denver11 = Denver2020Photos.objects.get(name="denver11")
    denver12 = Denver2020Photos.objects.get(name="denver12")
    denver13 = Denver2020Photos.objects.get(name="denver13")
    denver14 = Denver2020Photos.objects.get(name="denver14")
    return render(
        request,
        "denver2020.html",
        {
            "denver1": denver1,
            "denver2": denver2,
            "denver3": denver3,
            "denver4": denver4,
            "denver5": denver5,
            "denver6": denver6,
            "denver7": denver7,
            "denver8": denver8,
            "denver9": denver9,
            "denver10": denver10,
            "denver11": denver11,
            "denver12": denver12,
            "denver13": denver13,
            "denver14": denver14,
        },
    )


def la2021(request):
    la1 = LA2021Photos.objects.get(name="la1")
    la2 = LA2021Photos.objects.get(name="la2")
    la3 = LA2021Photos.objects.get(name="la3")
    la4 = LA2021Photos.objects.get(name="la4")
    la5 = LA2021Photos.objects.get(name="la5")
    la6 = LA2021Photos.objects.get(name="la6")
    la7 = LA2021Photos.objects.get(name="la7")
    la8 = LA2021Photos.objects.get(name="la8")
    la9 = LA2021Photos.objects.get(name="la9")
    la10 = LA2021Photos.objects.get(name="la10")
    la11 = LA2021Photos.objects.get(name="la11")
    la12 = LA2021Photos.objects.get(name="la12")
    return render(
        request,
        "la2021.html",
        {
            "la1": la1,
            "la2": la2,
            "la3": la3,
            "la4": la4,
            "la5": la5,
            "la6": la6,
            "la7": la7,
            "la8": la8,
            "la9": la9,
            "la10": la10,
            "la11": la11,
            "la12": la12,
        },
    )
