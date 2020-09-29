from django.db import models


# Create your models here.

class CreateStaff(models.Model):
    name = models.CharField(max_length=70,default='not selected')
    email = models.EmailField(max_length=250,default='not selected')
    gender = models.CharField(max_length=11,default='not selected')
    age=models.PositiveIntegerField(default=0)
    staffType=models.CharField(max_length=14,default='not selected')
    password = models.CharField(max_length=100,default='not selected')
