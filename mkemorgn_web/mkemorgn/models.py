from django.db import models

# Create your models here.
class About(models.Model):
    about_text = models.CharField(max_length=2000)
