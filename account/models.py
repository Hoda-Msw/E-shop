from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    email = models.EmailField()
    name = models.CharField(max_length=55)
    phone_no = models.CharField(max_length=11)
    national_code = models.CharField(max_length=10)
    address=models.TextField(null=True , blank=True)
    postal_code = models.CharField(max_length=12 , null=True , blank=True)

class Wallet(models.Model):
    profile = models.OneToOneField(Profile , on_delete=models.CASCADE)
    value = models.IntegerField()

class Transaction(models.Model):
    profile = models.ForeignKey(Profile , on_delete=models.CASCADE)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

