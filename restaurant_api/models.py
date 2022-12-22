from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=100)
    image = models.URLField()
    price = models.CharField(max_length=32)
    cuisine = models.CharField(max_length=100)
    number = models.IntegerField()