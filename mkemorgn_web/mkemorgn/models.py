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
    name = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Trips Page Photo URLs"

    def __str__(self):
        return self.trips_photo_url


class Detroit2020Photos(models.Model):
    photo_url = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Detroit 2020 Photos"

    def __str__(self):
        return self.photo_url


class Denver2020Photos(models.Model):
    photo_url = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Denver 2020 Photos"

    def __str__(self):
        return self.photo_url


class LA2021Photos(models.Model):
    photo_url = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "LA 2021 Photos"

    def __str__(self):
        return self.photo_url
