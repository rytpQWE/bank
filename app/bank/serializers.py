from rest_framework import serializers

from bank.models import BankAccount, Customer, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'account_from', 'account_to', 'comment', ]
        read_only_fields = ['id']


class BankAccountSerializer(serializers.ModelSerializer):
    history = TransactionSerializer(many=True, source='account_from', required=False)

    class Meta:
        model = BankAccount
        fields = ['id', 'user', 'balance', 'history', 'created_at']
        read_only_fields = ['id', 'user', 'balance', 'history', 'created_at']
        extra_kwargs = {'history': {"required": False, "allow_null": True}}


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['fname', 'lname', 'city', 'address']

    """Auto add user field(user_id)"""

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user
        return super(CustomerSerializer, self).create()
