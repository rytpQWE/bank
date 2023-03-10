from django.contrib import admin
from django.contrib.admin import ModelAdmin

from bank.models import BankAccount, Customer, Transaction


@admin.register(Transaction)
@admin.register(BankAccount)
@admin.register(Customer)
class BankAdmin(ModelAdmin):
    pass
