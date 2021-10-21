from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    avatar = models.ImageField(null = True)

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']


