from django.contrib import admin
from .models import User, Packages, Cryptocurrency, Payment, UserWallet, ConfirmPayment
# # Register your models here.

admin.site.register(User)
admin.site.register(Packages)
admin.site.register(Payment)
admin.site.register(Cryptocurrency)
admin.site.register(UserWallet)
admin.site.register(ConfirmPayment)
