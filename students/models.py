from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    phone = models.CharField(max_length=100)


class Marks(models.Model):
    student_id = models.IntegerField(null=False,blank=False)
    physics = models.CharField(max_length=100)
    chemistry = models.CharField(max_length=100)
    Maths = models.CharField(max_length=100)
    Botany = models.CharField(max_length=100)
    Zoology = models.CharField(max_length=100)
    English = models.CharField(max_length=100)
    Total = models.CharField(max_length=100)