from django.db import models

# Create your models here.
class Regions(models.Model):
    region = models.CharField(max_length=200)
    def __str__(self):
        return self.region

class AreaNames(models.Model):
    area = models.CharField(max_length=200)
    def __str__(self):
        return self.area
