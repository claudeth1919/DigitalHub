from rest_framework import serializers
from .models import Account, Balance, Transaction

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id','name','amount')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('fromAccount','toAccount','amount','sentAt')

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ('amount','balance','owner', 'createdAt')