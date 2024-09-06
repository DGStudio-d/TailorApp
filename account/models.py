from django.db import models

# Create your models here.

class ClientModel(models.Model):
    full_name=models.CharField(max_length=100)
    adress=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)

class TailorModel(models.Model):
    full_name = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)  # To store tailor ratings

    def __str__(self):
        return self.full_name
    
class SpecializeModel(models.Model):
    name=models.CharField(max_length=255)
    tailors=models.ManyToManyField(TailorModel)

