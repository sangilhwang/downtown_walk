from django.db import models

# Create your models here.

class EmpData(models.Model):
    borough = models.CharField(max_length = 20)
    mtolfirstfloor = models.FloatField()
    smallfirstfloor = models.FloatField()
    empdensity = models.FloatField()
    emptopopul = models.FloatField()
    
class DistrictData(models.Model):
    district_name = models.CharField(max_length = 10)
    large_b1_rent = models.FloatField()
    large_1_rent = models.FloatField()
    large_2_rent = models.FloatField()
    large_3_rent = models.FloatField()
    large_4_rent = models.FloatField()
    large_5_rent = models.FloatField()
    large_6to10_rent = models.FloatField()
    small_b1_rent = models.FloatField()
    small_1_rent = models.FloatField()
    small_2_rent = models.FloatField()
    district_size = models.FloatField()
    
class EmployeeData(models.Model):
    district_id = models.ForeignKey(DistrictData, on_delete=models.CASCADE)
    employee_count = models.IntegerField()
    company_count = models.IntegerField()
    employee_density = models.FloatField()
    company_density = models.FloatField()
    population_density = models.FloatField()
    employee_ratio = models.FloatField()
    
class FloatPopData(models.Model):
    district_id = models.ForeignKey(DistrictData, on_delete=models.CASCADE)
    subway_in = models.IntegerField()
    subway_out = models.IntegerField()
    bus_in = models.IntegerField()
    bus_out = models.IntegerField()
    subway_in_ratio = models.FloatField()
    subway_out_ratio = models.FloatField()
    bus_in_ratio = models.FloatField()
    bus_out_ratio = models.FloatField()
    combined_in_ratio = models.FloatField()
    combined_out_ratio = models.FloatField()
    total_ratio = models.FloatField()
    
class SeoulPopData(models.Model):
    district_id = models.ForeignKey(DistrictData, on_delete=models.CASCADE)
    s10 = models.IntegerField()
    s20 = models.IntegerField()
    s30 = models.IntegerField()
    s40 = models.IntegerField()
    s50 = models.IntegerField()
    s60 = models.IntegerField()
    s70 = models.IntegerField()
    s80_s90 = models.IntegerField()
    total = models.IntegerField()
    ratio_10s = models.FloatField()
    ratio_20s = models.FloatField()
    ratio_30s = models.FloatField()
    ratio_40s = models.FloatField()
    ratio_50s = models.FloatField()
    ratio_60s = models.FloatField()
    ratio_70s = models.FloatField()
    ratio_80s_to_90s = models.FloatField()
    ratio_total = models.FloatField()
    
class SeoulIncomeData(models.Model):
     district_id = models.ForeignKey(DistrictData, on_delete=models.CASCADE)
     district_income_per_person = models.IntegerField()
     district_income_gu= models.IntegerField()
     
class DistrictAgeData(models.Model):
    district_id = models.ForeignKey(DistrictData, on_delete=models.CASCADE)
    district_age = models.FloatField()
    
class StarbucksData(models.Model):
    district_id = models.ForeignKey(DistrictData, on_delete=models.CASCADE)
    store_count = models.IntegerField()
    store_ratio = models.FloatField()