from django.db import models

# Create your models here.
class AboutText(models.Model):
    about_text = models.TextField()

    class Meta:
        verbose_name_plural = "About Text"

    def __str__(self):
        return self.about_text


class AboutPhoto(models.Model):
    about_photo_url = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "About Photo URL"

    def __str__(self):
        return self.about_photo_url


class TripsPhotos(models.Model):
    trips_photo_url = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Trips Page Photo URLs"

    def __str__(self):
        return self.trips_photo_url
