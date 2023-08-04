from django.db import models

# Create your models here.

class Job(models.Model):
    logo = models.TextField()
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    skills = models.TextField()
    wfo = models.BooleanField(default=False)