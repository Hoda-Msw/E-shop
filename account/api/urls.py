from django.conf.urls import url
from django.contrib import admin

from .views import *

app_name = 'account'
urlpatterns = [
    # url(r'^$', FarmListAPIView.as_view(), name='list'),
    url(r'^wallet/$', WalletDetailAPIView.as_view(), name='wallet'),
    url(r'^transaction/$', TransactionListAPIView.as_view(), name='transaction'),
    url(r'^heartbeat/$', HeartbeatAPIView.as_view(), name='heartbeat'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),

]
