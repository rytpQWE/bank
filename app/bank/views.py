from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from bank.models import BankAccount
from bank.serializers import BankAccountSerializer


class AccountView(ReadOnlyModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
