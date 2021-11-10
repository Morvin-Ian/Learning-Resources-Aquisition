from rest_framework import serializers
from .models import Transaction


class MpesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['name' , 'amount']