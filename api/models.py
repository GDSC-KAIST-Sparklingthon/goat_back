from django.contrib.postgres.fields import ArrayField  
from django.db import models

# Create your models here.
class User(models.Model):
    #로그인 정보 추가하기
    id = models.CharField(primary_key=True, max_length=50)
    goat_age = models.IntegerField(default=0)
    hay_num = models.IntegerField(default=10)
    garden_array = models.JSONField(default=list, blank=True)
    subscription_end_date = models.DateField(null=True, blank=True)
    donated_goat_num = models.IntegerField(default=0)

class Donation(models.Model):
    donor = models.ForeignKey("User", on_delete=models.CASCADE)
    date = models.DateField()
    charity = models.CharField(max_length=50)