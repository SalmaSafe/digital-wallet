from datetime import datetime
import email
from locale import currency
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    address = models.TextField()
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10,null=True)
    age= models.PositiveSmallIntegerField()
    gender =models.CharField(max_length=7,null=True)

class Account(models.Model):
    account_number = models.CharField(max_length=20,null=True)
    account_name= models.CharField(max_length=30,null=True)
    balance = models.IntegerField()
    account_pin = models.PositiveSmallIntegerField(null=True)
    

class Wallet(models.Model):
    pin=models.SmallIntegerField()
    date_created=models.DateTimeField(default=datetime.now)
    balance = models.IntegerField() 
    customer=models.ForeignKey(Customer,related_name='customer_a', on_delete=models.CASCADE,null=True)
    currency = models.ForeignKey(Customer,related_name='customer_b', on_delete=models.CASCADE,null=True)  

class Transaction(models.Model):
    transaction_amount = models.IntegerField(null=True)
    date_time = models.DateTimeField(default=datetime.now,null=True)
    transaction_charge = models.IntegerField(null=True)
    destination_account = models.ForeignKey( Account,on_delete=models.CASCADE,related_name='account_a',null=True)
    origin_account =models.ForeignKey(Account, on_delete=models.CASCADE,related_name='account_b',null=True)
    receipt=models.ForeignKey(Account, on_delete=models.CASCADE,related_name='account_c',null=True)
    transaction_date = models.DateTimeField(default=datetime.now)
    transaction_charge = models.IntegerField(null=True)
    transaction_type = models.CharField(max_length=20,null=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE,null=True)
    transaction_ref = models.CharField(max_length=20,null=True)
class Card(models.Model):
    cardholder_number = models.IntegerField()
    expiry_date = models.DateField(default=datetime.now)
    cardholder_name= models.CharField(max_length=30,null=True)
    date_issued = models.DateTimeField(default=datetime.now)
    card_type = models.CharField(max_length=25,null=True)
    card_status = models.CharField(max_length=20,null=True)
    CVV_Security_code = models.IntegerField(null=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE,null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE,null=True)
    issuer = models.CharField(max_length=20,null=True)
    

    
class ThirdParty(models.Model):
    name =  models.CharField(max_length=15,null=True)
    balance = models.IntegerField(null=True)
    transaction_cost = models. IntegerField(null=True)
    account = models.IntegerField(null=True)
    phone_number =models.IntegerField(null=True)


class Notification(models.Model):
     date = models.DateTimeField()
     status = models.CharField(max_length=40,null=True)
     recipient = models.ForeignKey(ThirdParty, on_delete=models.CASCADE,null=True)
     name = models.CharField(max_length=15,null=True)
     id = models.PositiveSmallIntegerField(primary_key=True)

class Receipt(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE,related_name='transcation_b')
    receipt_date= models.DateTimeField(default=datetime.now)
    total_Amount= models.IntegerField(null=True)
    receipt_file = models.FileField(null=True)
    receipt_type = models.CharField(max_length=30,null=True)

class Loan(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    interest_rate = models.IntegerField(null=True)
    loan_balance = models.IntegerField(null=True)
    loan_term = models.IntegerField(null=True)
    pay_due_date = models.DateTimeField(default=datetime.now)
    guarantor = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)

class Reward(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    date_of_reward = models.DateTimeField(default=datetime.now)
    customer_id =models.IntegerField(null=True)
    gender=models.CharField(max_length=7,null=True)
    bonus_points=models.IntegerField(null=True)



