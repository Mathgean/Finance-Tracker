from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_type', 'amount', 'category', 'description']

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Optional'}),
        }
