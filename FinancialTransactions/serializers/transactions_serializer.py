from django.urls import path, include
from rest_framework import  serializers

from FinancialTransactions.models.entry_model import Entry

# Serializers define the API representation.
class EntrySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    amount = serializers.FloatField()
    date = serializers.DateField()
    class Meta:
        model = Entry
        fields = ['id', 'description', 'amount', 'date', 'category', 'account', ]