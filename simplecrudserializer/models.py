from operator import mod
from django.db import models

# Create your models here.
class Student(models.Model):
    prof_image = models.ImageField(upload_to='profilewithser')
    name = models.CharField(max_length=100,null=False,blank=False)
    age =models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=100,default='')
