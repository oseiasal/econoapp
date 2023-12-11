#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework import routers

from FinancialTransactions import viewsets

router = routers.SimpleRouter()
router.register(r"entry", viewsets.EntryViewSet, basename="entry")
router.register(r"expense", viewsets.ExpenseViewSet, basename="expense")


urlpatterns = [
    path("", include(router.urls)),
]