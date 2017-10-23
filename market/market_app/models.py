from django.db import models

# Create your models here.
class Goods(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    descrition = models.CharField(max_length=500, null=True, blank=True)
    cpu = models.CharField(max_length=50, null=True, blank=True)
    cpu_freq = models.CharField(max_length=20, null=True, blank=True)
    ram = models.CharField(max_length=20, null=True, blank=True)
    hdd = models.CharField(max_length=20, null=True, blank=True)
    display = models.CharField(max_length=10, null=True, blank=True)
    videocard = models.CharField(max_length=50, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    dvd = models.BooleanField(default=False)
    lte = models.BooleanField(default=False)
    bluetooth = models.BooleanField(default=True)
    wifi = models.BooleanField(default=True)
    price = models.FloatField(default=0)
    image = models.FilePathField(null=True, blank=True)