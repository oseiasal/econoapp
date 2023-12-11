from rest_framework.viewsets import ModelViewSet
from FinancialTransactions.models.expense_model import Expense

from FinancialTransactions.serializers.expense_serializer import ExpenseSerializer
# from models.expense_model import Expense
# from serializers.expense_serializer import ExpenseSerializer

class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()