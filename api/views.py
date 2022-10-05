from django.shortcuts import render
from rest_framework import viewsets
from wallet.models import Customer
from wallet.models import Wallet
from wallet.models import Account
from wallet.models import Card
from wallet.models import Transaction
from wallet.models import Loan
from wallet.models import Receipt
from wallet.models import Notification
from .serializers import CustomerSerilaizers
from .serializers import WalletSerilaizers
from .serializers import AccountSerilaizers
from .serializers import CardSerilaizers
from .serializers import TransactionSerilaizers
from .serializers import LoanSerilaizers
from .serializers import ReceiptSerilaizers
from .serializers import NotificationSerilaizers

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerilaizers

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerilaizers

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerilaizers

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerilaizers

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerilaizers

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerilaizers

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerilaizers

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = CustomerSerilaizers
                                 