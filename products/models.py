from itertools import product
from operator import mod
from statistics import mode
from django.db import models

# Create your models here.
class TagModel(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)

class ProductModel(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    desc = models.CharField(max_length=100,null=False,blank=False)
    tags = models.ManyToManyField(TagModel)

class ProductVariants(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    price = models.CharField(max_length=100,null=False,blank=False)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)