from django.db import models
class BankAccount(models.Model):
    account_name = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.account_name