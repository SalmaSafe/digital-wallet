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
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender =models.CharField(max_length=7,null=True)
    customer_id= models.CharField(max_length=15,null=True)
    nationality=models.CharField(max_length=15,null=True)
    profile_picture= models.ImageField(upload_to='profile_picture',null=True)

class Account(models.Model):
    account_number = models.CharField(max_length=20,null=True)
    account_name= models.CharField(max_length=30,null=True)
    balance = models.IntegerField()
    account_pin = models.PositiveSmallIntegerField(null=True)
    account_choices=(
        ('w', 'withdraw'),
        ('S', 'Savings'),
        ('D', 'Deposit')

    )
    account_type= models.CharField(max_length=15, choices=account_choices,null=True)

    def deposit(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
       else:
           self.balance += amount
           self.save()
           message = f"You have deposited {amount}, your new balance is {self.balance}"
           status = 200
       return message, status
    def transfer(self, destination, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
      
       elif amount < self.balance:
           message =  "Insufficient balance"
           status = 403
      
       else:
           self.balance -= amount
           self.save()
           destination.deposit(amount)
          
           message = f"You have transfered {amount}, your new balance is {self.balance}"
           status = 200
       return message, status 
    def withdraw(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
       else:
           self.balance -= amount
           self.save()
           message = f"You have withdrawn {amount}, your new balance is {self.balance}"
           status = 200
       return message, status 
    # def transfer(self, destination, amount):
    #    if amount <= 0:
    #        message =  "Invalid amount"
    #        status = 403
      
    #    elif amount < self.balance:
    #        message =  "Insufficient balance"
    #        status = 403
      
    #    else:
    #        self.balance -= amount
    #        self.save()
    #        destination.withdraw(amount)
          
    #        message = f"You have withdrawn {amount}, your new balance is {self.balance}"
    #        status = 200
    #    return message, status
    def request_loan(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
       else:
           self.balance += amount
           self.save()
           message = f"Your loan of {amount} was granted successfully, your new balance is {self.balance}"
           status = 200
       return message, status 

    def repay_loan(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
       else:
           self.balance -= amount
           self.save()
           message = f"You have used {amount} to repay for your loan, your new balance is {self.balance}"
           status = 200
       return message, status  
    def buy_airtime(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
       else:
           self.balance -= amount
           self.save()
           message = f"You have bought airtime for {amount}, your new balance is {self.balance}"
           status = 200
       return message, status      


    


    

class Wallet(models.Model):
    pin=models.SmallIntegerField()
    date_created=models.DateTimeField(default=datetime.now)
    balance = models.IntegerField() 
    account_wallet = models.ForeignKey("Account",on_delete= models.CASCADE, related_name= "account_wallet", null=True)    
    CURRENCY_CHOICES = (
        ('K','Shilling'),
        ('$','Dollar'),
        ('EU','Euros'),
    )
    currency = models.CharField(max_length= 15, choices= CURRENCY_CHOICES,null=True)  


class Transaction(models.Model):
    transaction_amount = models.IntegerField(null=True)
    date_time = models.DateTimeField(default=datetime.now,null=True)
    transaction_charge = models.IntegerField(null=True)
    wallet_one = models.ForeignKey("Wallet",on_delete= models.CASCADE,related_name="Transaction_wallet",null=True)
    destination_account = models.ForeignKey( Account,on_delete=models.CASCADE,related_name='account_a',null=True)
    origin_account =models.ForeignKey(Account, on_delete=models.CASCADE,related_name='account_b',null=True)
    receipt=models.ForeignKey(Account, on_delete=models.CASCADE,related_name='account_c',null=True)
    transaction_date = models.DateTimeField(default=datetime.now)
    transaction_charge = models.IntegerField(null=True)
    TRASACTION_TYPE_CHOICES = (
        ('D','Debit'),
        ('C','Credit'),
    )
    transaction_type = models.CharField(max_length=20, choices= TRASACTION_TYPE_CHOICES,null=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE,null=True)
    transaction_ref = models.CharField(max_length=20,null=True)


class Card(models.Model):
    cardholder_number = models.IntegerField()
    expiry_date = models.DateField(default=datetime.now)
    cardholder_name= models.CharField(max_length=30,null=True)
    date_issued = models.DateTimeField(default=datetime.now)
    CARD_TYPE_CHOICES = (
        ('C','Credit card'),
        ('D','Debit card'),
    )
    card_type = models.CharField(max_length=25,choices=CARD_TYPE_CHOICES, null=True)
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



