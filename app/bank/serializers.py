from rest_framework import serializers

from bank.models import BankAccount, Customer


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['user', 'balance']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['fname, lname', 'city', 'address']