from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
class SubjectModel(models.Model):
    stu_id=models.IntegerField(null=False,blank=False)
    subject=models.CharField(max_length=20,null=False,blank=False)
    mark=models.FloatField(default=0.0)
    # english=models.FloatField(default=0.0)
    # maths=models.FloatField(default=0.0)
    # physics=models.FloatField(default=0.0)
    # chemistry=models.FloatField(default=0.0)
    # biology=models.FloatField(default=0.0)
    # arabic=models.FloatField(default=0.0)
    