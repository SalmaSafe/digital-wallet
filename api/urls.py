
from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewSet
from .views import WalletViewSet
from .views import AccountViewSet
from .views import CardViewSet
from .views import TransactionViewSet
from .views import LoanViewSet
from .views import ReceiptViewSet
from .views import NotificationViewSet


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'wallets', WalletViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'cards', CardViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'receipts', ReceiptViewSet)
router.register(r'notifications', NotificationViewSet)



urlpatterns =[
    path('', include (router.urls)),
]

