from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from bank.models import BankAccount
from bank.serializers import BankAccountSerializer


class AccountView(ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
