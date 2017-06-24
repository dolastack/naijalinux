from django.db import models

# Create your models here.
class OpenSourceProject(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
