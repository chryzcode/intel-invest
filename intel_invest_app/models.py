from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=250, null=True)
    email = models.EmailField(unique=True)


    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email + ' ' + str(self.full_name)

class Packages(models.Model):
    package_name = models.CharField(max_length=250)
    package_price = models.IntegerField()
    package_description = models.TextField(null=True, blank=True)
    investors = models.ManyToManyField(User, related_name='investors', blank=True)

    def __str__(self):
        return self.package_name

class Cryptocurrency(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshot/user-payment/')
    cryptocurrency = models.CharField(max_length=200)
    transanction_hash = models.CharField(max_length=300)
    package = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username + ' ' + str('wallets') + ' ' + str(self.user.email)



class UserWallet(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    bitcoin = models.CharField(max_length=250, null=True, blank=True)
    ethereum = models.CharField(max_length=250, null=True, blank=True)
    litecoin = models.CharField(max_length=250, null=True, blank=True)
    bnb = models.CharField(max_length=250, null=True, blank=True)
    busd = models.CharField(max_length=250, null=True, blank=True)
    usdt = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.user.username  + ' ' + str('wallets') + ' ' + str(self.user.email)




class ConfirmPayment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    reciever_email = models.EmailField(max_length=250)
    reciever_account = models.CharField(max_length=350)
    body = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    screenshot = models.ImageField(upload_to='screenshot/confirm-payment/')

    def __str__(self):
        return self.user  + ' ' + str('payment to') + ' ' + self.reciever
