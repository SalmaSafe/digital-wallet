from django.urls import path
from .views import register_card, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet
from .views import register_account

urlpatterns=[
    path("register/", register_customer, name="registration"),
    path("registerreward/", register_reward, name="reward"),
    path("registeraccount/", register_account, name="account"),
    path("registerwallet/", register_wallet, name="wallet"),
    path("registercard/", register_card, name="card"),
    path("registernotification/", register_notification, name="notification"),
    path("registertransaction/", register_transaction, name="transaction"), 
    path("registerthirdparty/", register_thirdparty, name="thirdparty"),
    path("registerreceipt/", register_receipt, name="receipt"),
    path("registerloan/", register_loan, name="loan"),
   

]
