from django import forms
from .models import Expense, Income


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_type', 'amount', 'category', 'description']

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Optional'}),
        }


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['income_type', 'amount', 'category', 'description']

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Optional'}),
        }