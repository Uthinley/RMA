from django.db import models

# Create your models here.
class GoldMaster(models.Model):
    Particulars= models.CharField(max_length=1200)
    Units = models.CharField(max_length=100)

    


class GoldRates(models.Model):
    date = models.DateField(auto_now_add=True)
    # Rate = models.DecimalField(max_digits="20",decimal_places=2)
    Rate = models.IntegerField()
    ParticularsId = models.ForeignKey(GoldMaster, related_name="golddetails", on_delete=models.CASCADE)

   
    






