from rest_framework import serializers

from bank.models import BankAccount, Customer


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['user', 'balance']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['fname', 'lname', 'city', 'address']
    """Auto add user field(user_id)"""
    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user
        return super(CustomerSerializer, self).create()