from django.contrib import admin
from .models import (
    IndexPhotos,
    AboutPhoto,
    TripsPhotos,
    Detroit2020Photos,
    Denver2020Photos,
    LA2021Photos,
)

# Register your models here.
admin.site.register(IndexPhotos)
admin.site.register(AboutPhoto)
admin.site.register(TripsPhotos)
admin.site.register(Detroit2020Photos)
admin.site.register(Denver2020Photos)
admin.site.register(LA2021Photos)
