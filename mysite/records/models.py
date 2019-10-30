from django.db import models

# Create your models here.
class Record(models.Model):
    title               = models.TextField(default="Default Artist")
    artist              = models.TextField()
    duration            = models.TextField()
    yearOfPublication   = models.TextField()
