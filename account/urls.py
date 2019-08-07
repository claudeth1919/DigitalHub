from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('accounts', views.AccountView)
router.register('balances', views.BalanceView)
router.register('transactions', views.TransactionView)

urlpatterns = [
    path('',include(router.urls))
]
