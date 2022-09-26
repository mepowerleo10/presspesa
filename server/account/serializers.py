from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "uuid",
            "username",
            "email",
            "phone_no",
            "birth_date",
            "address",
        ]
