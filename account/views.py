from django.shortcuts import render
from rest_framework import viewsets
from .models import Account, Balance, Transaction
from .serializers import AccountSerializer, BalanceSerializer, TransactionSerializer

class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class BalanceView(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer

class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer