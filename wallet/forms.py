
from django import forms
from .models import Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
from .models import Account
class CustomerRegistrationForm(forms.ModelForm):
    class Meta:# class inside a class - provides data about a customer
        model = Customer
        fields = '__all__'

class AccountRegistrationForm(forms.ModelForm):
    class Meta:# class inside a class - provides data about a customer
        model = Account
        fields = '__all__'       

class TransactionRegistrationForm(forms.ModelForm):
    class Meta:# class inside a class - provides data about a customer
        model = Transaction
        fields = '__all__'          

class WalletRegistrationForm(forms.ModelForm):
    class Meta:# class inside a class - provides data about a customer
        model = Wallet
        fields = '__all__'  

class CardRegistrationForm(forms.ModelForm):
    class Meta:# class inside a class - provides data about a customer
        model = Card
        fields = '__all__'  

class NotificationRegistrationForm(forms.ModelForm):
    class Meta:# class inside a class - provides data about a customer
        model = Notification
        fields = '__all__'                  

class ThirdPartyRegistrationForm(forms.ModelForm):
    class Meta:# class inside a class - provides data about a customer
        model = ThirdParty
        fields = '__all__'  

class ReceiptRegistrationForm(forms.ModelForm):
    class Meta:# class inside a class - provides data about a customer
        model = Receipt
        fields = '__all__'  

class LoanRegistrationForm(forms.ModelForm):
    class Meta:# class inside a class - provides data about a customer
        model = Loan
        fields = '__all__'  

class RewardRegistrationForm(forms.ModelForm):
    class Meta:# class inside a class - provides data about a customer
        model = Reward
        fields = '__all__'  


