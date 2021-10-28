from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=250, null=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']
