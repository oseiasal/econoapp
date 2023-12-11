from rest_framework.viewsets import ModelViewSet
from FinancialTransactions.models.entry_model import Entry

from FinancialTransactions.serializers.transactions_serializer import EntrySerializer

class EntryViewSet(ModelViewSet):

    serializer_class = EntrySerializer
    queryset = Entry.objects.all()