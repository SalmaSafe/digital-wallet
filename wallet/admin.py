from django.contrib import admin

# Register your models here.
# Add model to admin dashboard.
from .models import  Account, Card, Customer, Loan, Notification, Receipt, ThirdParty, Transaction, Wallet,Reward
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','age','email',)
    search_fields = ('first_name', 'last_name',)
admin.site.register(Customer, CustomerAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_name','balance',)
    search_fields = ('account_number','account_name',)
admin.site.register(Account, AccountAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ('pin','currency',)
    search_fields = ('pin','curreny',)
admin.site.register(Wallet, WalletAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_amount','date_time',)
    search_fields = ('transaction_amount','date_time',)
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ('cardholder_number','expiry_date',)
    search_fields = ('cardholder_number','expiry_date',)
admin.site.register(Card,CardAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display = ('name','balance',)
    search_fields = ('name','balance',)
admin.site.register(ThirdParty, ThirdPartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('date','status',)
    search_fields = ('date','status',)
admin.site.register(Notification, NotificationAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('transaction','receipt_date',)
    search_fields = ('transaction','receipt_date',)
admin.site.register(Receipt, ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('wallet','interest_rate',)
    search_fields = ('wallet','interest_rate',)
admin.site.register(Loan, LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display = ('transaction','date_of_reward',)
    search_fields = ('transaction','date_of_reward',)
admin.site.register(Reward, RewardAdmin)



# class CustomerAdmin(admin.ModelAdmin):
#      list_display =('first_name', 'last_name','age','email',)
#      search_fields = ('first_name','last_name')

# admin.site.register(Customer,CustomerAdmin)
