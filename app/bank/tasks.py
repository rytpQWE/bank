from celery import shared_task
from django.db import transaction

from bank.models import BankAccount


@shared_task()
def bank_interest():
    accounts = BankAccount.objects.all()
    for account in accounts:
        with transaction.atomic():
            percent = 10
            interest = account.balance * percent / 100
            update_balance = account.balance + interest
            account.balance += update_balance
            trans = BankAccount.objects.create(
                account=account,
                amount=interest,
                percent=percent,
            )
            account.save()
