from django.db import models

# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    unit = models.IntegerField()
    price = models.FloatField()
    stock = models.IntegerField()
    notes = models.CharField(max_length=255)