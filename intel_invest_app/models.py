from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=250, null=True)
    email = models.EmailField(unique=True)


    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']

class Packages(models.Model):
    package_name = models.CharField(max_length=250)
    package_price = models.IntegerField()
    package_description = models.TextField(null=True, blank=True)
    investors = models.ManyToManyField(User, related_name='investors', blank=True)

    def __str__(self):
        return self.package_name



