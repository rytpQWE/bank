from django.contrib.auth.models import User
from django.db import models


class BankAccount(models.Model):
    # You cannot delete user with money
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User\'s account: {self.user} id {self.pk}'


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


# Transactions history
class Transaction(models.Model):
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    created_at = models.DateTimeField(auto_now_add=True)
    account_from = models.ForeignKey(
        BankAccount,
        on_delete=models.CASCADE,
        related_name='account_from',
    )
    account_to = models.ForeignKey(
        BankAccount,
        on_delete=models.CASCADE,
        related_name='account_to',
    )
    comment = models.CharField(max_length=256)

    class Meta:
        ordering = ['-pk']


# Bank interests history
class Interest(models.Model):
    account = models.ForeignKey(
        BankAccount,
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )
    percent = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
