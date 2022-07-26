import email
from pyexpat import model
from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    age= models.PositiveSmallIntegerField()

class Account(models.Model):
    account_number = models.CharField(max_length=20)
    account_name= models.CharField(max_length=30)
    balance = models.IntegerField()

class Wallet(models.Model):
    pin=models.SmallIntegerField(max_length=10)
    date_created=models.DateTimeField()
    amount = models.IntegerField()   

class Transaction(models.Model):
    transaction_amount = models.IntegerField()
    date_time = models.DateTimeField()
    transaction_charge = models.IntegerField()
class Card(models.Model):
    cardholder_number = models.IntegerField()
    expiry_date = models.DateField()
    cardholder_name= models.CharField()
    
class ThirdParty(models.Model):
    balance = models.IntegerField()
    transaction_cost = models. IntegerField()
    account = models.IntegerField()

class Notification(models.Model):
     date = models.DateTimeField()
     status = models.CharField()
     recepient = models.CharField()

class Receipt(models.Model):
    transaction = models.ForeignKey()
    receipt_date= models.DateTimeField()
    total_Amount= models.IntegerField()

class Loan(models.Model):
    wallet = models.ForeignKey()
    interest_rate = models.IntegerField()
    loan_balance = models.IntegerField()

class Reward(models.Model):
    transaction = models.ForeignKey()
    date_of_reward = models.DateTimeField()
    recepient = models.ForeignKey()       



