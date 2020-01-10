from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )
from account.models import *

class WalletDetailSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = [
            'value'
        ]

class TransactionDetailSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'amount'
        ]
class ProfileViewSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'email',
            'name',
            'phone_no',
            'national_code',
            'address',
            'postal_code',
        ]
