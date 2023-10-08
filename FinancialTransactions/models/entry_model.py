from django.db import models
from django.utils import timezone
from .category_model import Category


class Entry(models.Model):
    description = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

