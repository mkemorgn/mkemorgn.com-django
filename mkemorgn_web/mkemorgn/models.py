from django.db import models

# Create your models here.
class AboutText(models.Model):
    about_text = models.TextField()

    class Meta:
        verbose_name_plural = "about"

    def __str__(self):
        return self.about_text


class AboutPhoto(models.Model):
    about_photo_url = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "about url"

    def __str__(self):
        return self.about_photo_url
