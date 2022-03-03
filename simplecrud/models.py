from django.db import models

# Create your models here.


class ProductsModel(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    price = models.FloatField(default=0.0)
    description = models.TextField()


