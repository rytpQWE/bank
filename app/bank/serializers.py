from rest_framework import serializers

from bank.models import BankAccount, Customer, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'account_from', 'account_to', 'comment', ]
        read_only_fields = ['id']


class BankAccountSerializer(serializers.ModelSerializer):
    history = TransactionSerializer(many=True, source='account_from')

    class Meta:
        model = BankAccount
        fields = ['user', 'balance', 'history']
        read_only_fields = ['user', 'balance', 'history']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['fname', 'lname', 'city', 'address']

    """Auto add user field(user_id)"""

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user
        return super(CustomerSerializer, self).create()
