from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from wallet.models import Customer
from wallet.models import Wallet
from wallet.models import Account
from wallet.models import Card
from wallet.models import Transaction
from wallet.models import Loan
from wallet.models import Receipt
from wallet.models import Notification



class CustomerSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name','last_name', 'age','email')

class WalletSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('balance','account_wallet','currency')  

class AccountSerilaizers(serializers.ModelSerializer):
    class Meta:
        model =Account
        fields = ('account_name','account_number','balance')  

class CardSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('cardholder_name','cardholder_number', 'expiry_date','date_issued','card_type')  

class TransactionSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('transaction_amount','transaction_charge','transaction_account','receipt','date_time')    

class LoanSerilaizers(serializers.ModelSerializer):
    class Meta:
        model =Loan
        fields = ('wallet','pay_due_date','loan_balance','interest_rate') 

class ReceiptSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('transaction','total_amount','receipt_file','receipt_date','receipt_type')  

class NotificationSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields =('date','status','receipt','name','id')                                     



