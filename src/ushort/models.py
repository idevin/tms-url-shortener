from django.db import models


# Create your models here.
class Url(models.Model):
    url = models.TextField(null=False, unique=True)
    hash = models.CharField(null=True, max_length=62)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    clicks = models.IntegerField(default=0)
