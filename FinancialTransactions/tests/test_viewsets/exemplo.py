from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from FinancialTransactions.factories import CategoryFactory, EntryFactory
from FinancialTransactions.models.entry_model import Entry

class MyModelViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = CategoryFactory()
        self.entry = EntryFactory(category=self.category)

    def test_entry_api_exist(self):
        response = self.client.get('/api/v1/entry/')   
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(len(response.data), 1)

    def test_expense_api_exist(self):
        response = self.client.get('/api/v1/expense/')   
        self.assertEqual(response.status_code, status.HTTP_200_OK) 