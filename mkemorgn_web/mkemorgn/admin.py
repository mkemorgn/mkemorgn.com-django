from django.contrib import admin
from .models import AboutText, AboutPhoto, TripsPhotos, DetroitPhotos

# Register your models here.
admin.site.register(AboutText)
admin.site.register(AboutPhoto)
admin.site.register(TripsPhotos)
admin.site.register(DetroitPhotos)
