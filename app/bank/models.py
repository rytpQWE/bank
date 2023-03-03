from django.contrib.auth.models import User
from django.db import models


class BankAccount(models.Model):
    # You cannot delete user with money
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return f'User\'s account: {self.user}'


class Customer(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Customer: {self.fname} {self.lname}'
