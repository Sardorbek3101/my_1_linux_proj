from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUSer(AbstractUser):
    profile_picture = models.ImageField()
    tel_num = models.CharField(max_length=17)