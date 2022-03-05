from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)

class Mark(models.Model):
    student_id = models.CharField(max_length=100)
    sub_name = models.CharField(max_length=100)
    sub_mark = models.CharField(max_length=100)