from django.contrib import admin
from .models import User, Packages, Cryptocurrency, Payment
# # Register your models here.

admin.site.register(User)
admin.site.register(Packages)
admin.site.register(Payment)
admin.site.register(Cryptocurrency)
