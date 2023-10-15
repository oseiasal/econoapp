from django.contrib import admin

# Register your models here.
from .models import BankAccount, Category, Entry, Expense

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('description','account' , 'amount', 'date', 'category')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date', 'category')
