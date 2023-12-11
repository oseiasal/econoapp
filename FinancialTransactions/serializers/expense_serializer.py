from rest_framework import  serializers

from FinancialTransactions.models.expense_model import Expense
# from models.expense_model import Expense

class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = "__all__"
