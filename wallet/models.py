import email
from locale import currency
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)
    age= models.PositiveSmallIntegerField()
    gender =models.CharField(max_length=7)

class Account(models.Model):
    account_number = models.CharField(max_length=20)
    account_name= models.CharField(max_length=30)
    balance = models.IntegerField()
    account_pin = models.PositiveSmallIntegerField()
    

class Wallet(models.Model):
    pin=models.SmallIntegerField()
    date_created=models.DateTimeField()
    balance = models.IntegerField() 
    customer=models.ForeignKey(default=1, on_delete=models.CASCADE, to=Customer)
    currency = models.ForeignKey(default=1, on_delete=models.CASCADE, to=currency)  

class Transaction(models.Model):
    transaction_amount = models.IntegerField()
    date_time = models.DateTimeField()
    transaction_charge = models.IntegerField()
    destination_account = models.ForeignKey(default=1, on_delete=models.CASCADE, to=Account)
    origin_account =models.ForeignKey(default=1, on_delete=models.CASCADE, to=Account)
    receipt=models.ForeignKey(default=1, on_delete=models.CASCADE, to=Receipt)
    transaction_date = models.DateTimeField()
    transaction_charge = models.IntegerField()
    transaction_type = models.CharField(max_length=20)
    wallet = models.ForeignKey(default=1, on_delete=models.CASCADE, to=Wallet)
    transaction_ref = models.CharField(max_length=20)
class Card(models.Model):
    cardholder_number = models.IntegerField()
    expiry_date = models.DateField()
    cardholder_name= models.CharField(max_length=30)
    date_issued = models.DateTimeField()
    card_type = models.CharField(max_length=25)
    card_status = models.CharField(max_length=20)
    CVV_Security_code = models.IntegerField()
    wallet = models.ForeignKey(default=1, on_delete=models.CASCADE, to=Wallet)
    account = models.ForeignKey(default=1, on_delete=models.CASCADE, to=Account)
    issuer = models.CharField(max_length=20)
    

    
class ThirdParty(models.Model):
    name =  models.CharField(max_length=15)
    balance = models.IntegerField()
    transaction_cost = models. IntegerField()
    account = models.IntegerField()
    phone_number =models.IntegerField()


class Notification(models.Model):
     date = models.DateTimeField()
     status = models.CharField(max_length=40)
     recipient = models.ForeignKey(default=1, on_delete=models.CASCADE, to=ThirdParty)
     name = models.CharField(max_length=15)
     id = models.PositiveSmallIntegerField()

class Receipt(models.Model):
    transaction = models.ForeignKey(default=1, on_delete=models.CASCADE, to=Transaction)
    receipt_date= models.DateTimeField()
    total_Amount= models.IntegerField()
    receipt_file = models.FileField()
    receipt_type = models.CharField()

class Loan(models.Model):
    wallet = models.ForeignKey(default=1, on_delete=models.CASCADE, to=Wallet)
    interest_rate = models.IntegerField()
    loan_balance = models.IntegerField()
    loan_term = models.IntegerField()
    pay_due_date = models.DateTimeField()
    guarantor = models.ForeignKey(default=1, on_delete=models.CASCADE, to=Customer)

class Reward(models.Model):
    transaction = models.ForeignKey(default=1, on_delete=models.CASCADE, to=Transaction)
    date_of_reward = models.DateTimeField()
    customer_id =models.IntegerField()
    gender=models.CharField(max_length=7)
    bonus_points=models.IntegerField()



