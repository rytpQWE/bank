from django.db import transaction

from bank.models import Transaction


def make_trans(account_from, account_to, amount, comment):
    if account_from.balance < amount:
        raise (ValueError('Not enough money'))
    if account_from == account_to:
        raise (ValueError('Choose another account'))

    with transaction.atomic():
        changed_balance_from = account_from.balance - amount
        account_from.balance = changed_balance_from
        account_from.save()

        changed_balance_to = account_to.balance + amount
        account_to.balance = changed_balance_to
        account_to.save()

        trans = Transaction.objects.create(
            amount=amount,
            account_from=account_from,
            account_to=account_to,
            comment=comment,
        )
    return trans
