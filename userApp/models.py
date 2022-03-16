from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class UserDetails(AbstractUser):

    mobile = models.CharField(unique=True,max_length=12,null=False)
    address = models.TextField(null=True,blank=True)