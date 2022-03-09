from django.db import models

# Create your models here.
class About(models.Model):
    about_text = models.TextField()

    class Meta:
        verbose_name_plural = "about"

    def __str__(self):
        return self.about_text
