from django.db import models

# Create your models here.

class EmpData(models.Model):
    borough = models.CharField(max_length = 20)
    mtolfirstfloor = models.FloatField()
    smallfirstfloor = models.FloatField()
    empdensity = models.FloatField()
    emptopopul = models.FloatField()