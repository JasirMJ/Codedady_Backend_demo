from django.db import models

# Create your models here.

class TagsModel(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)

class ProductsRelationModel(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    description = models.TextField()
    tags = models.ManyToManyField(TagsModel)

class ProductVariant(models.Model):
    name = models.CharField(max_length=5,null=False,blank=False)
    price = models.FloatField(default=0.0)
    product = models.ForeignKey(ProductsRelationModel,on_delete=models.CASCADE,null=True,blank=True)


# alter table application_tblapplication auto_increment=1000;