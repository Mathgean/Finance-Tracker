from django import forms
from .models import Expense, Income
from django.utils.dates import MONTHS


class MonthYearForm(forms.Form):
    MONTH_CHOICES = [(str(i), MONTHS[i]) for i in range(1, 13)]
    YEAR_CHOICES = [(str(i), str(i)) for i in range(2020, 2051)]

    month = forms.ChoiceField(choices=MONTH_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)


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


