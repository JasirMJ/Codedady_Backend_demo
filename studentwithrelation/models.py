from django.db import models

# Create your models here.
class Student(models.Model):
    prof_image = models.ImageField(upload_to='profile')
    name = models.CharField(max_length=100,null=False,blank=False)


class Marks(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    maths_mrk = models.CharField(max_length=100,null=False,default=0,blank=False)
    physics_mrk = models.CharField(max_length=100,null=False,default=0,blank=False)
    chemistry_mrk = models.CharField(max_length=100,null=False,default=0,blank=False)
    english_mrk = models.CharField(max_length=100,null=False,default=0,blank=False)
    botany_mrk = models.CharField(max_length=100,null=False,default=0,blank=False)
    zoology_mrk = models.CharField(max_length=100,null=False,default=0,blank=False)
    semester = models.CharField(max_length=100,null=False,default=0,blank=False)
    total = models.CharField(max_length=100,null=False,default=0,blank=False)

