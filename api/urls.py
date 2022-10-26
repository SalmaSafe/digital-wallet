
from django.urls import path,include
from rest_framework import routers
from .views import AccountBuyAirtimeView, AccountDepositView, AccountRepayLoanView, AccountRequestLoanView, AccountTransferView, AccountWithdrawView, CustomerViewSet
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
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
    path("withdraw/", AccountWithdrawView.as_view(), name="withdraw-view"),
    path("transfer/", AccountTransferView.as_view(), name="transfer-view"),
    path("request_loan/", AccountRequestLoanView.as_view(), name="request-loan-view"),
    path("repay_loan/", AccountRepayLoanView.as_view(), name="repay-loan-view"),
    path("buy_airtime/", AccountBuyAirtimeView.as_view(), name="buy-airtime-view"),


]

