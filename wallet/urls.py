from django.urls import path

from . import views


urlpatterns=[
    path("register/", views.register_customer, name="registration"),
    path("registerreward/", views.register_reward, name="reward"),
    path("registeraccount/", views.register_account, name="account"),
    path("registerwallet/", views.register_wallet, name="wallet"),
    path("registercard/", views.register_card, name="card"),
    path("registernotification/",views.register_notification, name="notification"),
    path("registertransaction/", views.register_transaction, name="transaction"), 
    path("registerthirdparty/", views.register_thirdparty, name="thirdparty"),
    path("registerreceipt/", views.register_receipt, name="receipt"),
    path("registerloan/", views.register_loan, name="loan"),
    path("customers/", views.list_customers,name="customer_list"),
    path("accounts/", views.list_account,name="account_list"),
    path("wallets/", views.list_wallet,name="wallet_list"),
    path("transactions/", views.list_transaction,name="transaction_list"),
    path("cards/", views.list_card,name="card_list"),
    path("thirdpartys/", views.list_thirdparty,name="thirdparty_list"),
    path("notifications/", views.list_notification,name="notification_list"),
    path("receipts/", views.list_receipt,name="receipt_list"),
    path("rewards/", views.list_reward,name="reward_list"),
      

]
