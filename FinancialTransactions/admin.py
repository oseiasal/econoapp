from django.contrib import admin

# Register your models here.
from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'date', 'category')

admin.site.register(Entry, EntryAdmin)