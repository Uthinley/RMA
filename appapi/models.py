from django.db import models

# Create your models here.

class GoldRates(models.Model):
    Particulars = models.CharField(max_length=100)
    Units = models.CharField(max_length=50)
    Rate = models.IntegerField()
