from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=60)
    avAge = models.CharField(max_length=60)
    avDailyIncomeInUSD = models.CharField(max_length=60)
    avDailyIncomePopulation = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Report(models.Model):
    region = models.OneToOneField(Region, on_delete=models.CASCADE)
    periodType = models.CharField(max_length=60)
    timeToElpase = models.CharField(max_length=60)
    reportedCases = models.CharField(max_length=60)
    Population = models.CharField(max_length=60)
    totalHospitalBeds = models.CharField(max_length=60)
    
    def __str__(self):
        return self.region.name