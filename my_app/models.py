from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass


class Cars(models.Model):
    model = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    age = models.IntegerField(blank=True)
