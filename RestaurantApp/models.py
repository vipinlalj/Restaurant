from django.db import models

# Create your models here.
class CatDB(models.Model):
    CatName = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(null=True, blank=True)
class FoodDB(models.Model):
    CatName = models.CharField(max_length=50, null=True, blank=True)
    FoodName = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(max_length=3, null=True, blank=True)
    Image = models.ImageField(null=True, blank=True)
