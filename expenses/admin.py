from django.contrib import admin
from .models import Expense, Category

# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'description', 'owner', 'category')
    search_fields = ('amount', 'date', 'description', 'owner', 'category')

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category)