from django.contrib.postgres.fields import ArrayField  
from django.db import models

# Create your models here.
class User(models.Model):
    #로그인 정보 추가하기
    id = models.CharField(primary_key=True, max_length=50)
    goat_age = models.IntegerField(default=0)
    grass_num = models.IntegerField(default=0)
    garden_array = ArrayField(models.BooleanField(max_length=1), size=81, default=[False]*81) 
    #여기서부터 optional
    subscription_end_date = models.DateField(null=True, blank=True)
    donated_goat_num = models.IntegerField(default=0)

class Donation(models.Model):
    donor = models.ForeignKey("User", on_delete=models.CASCADE)
    date = models.DateField()
    charity = models.CharField(max_length=50)