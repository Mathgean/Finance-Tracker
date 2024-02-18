from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Clothing', 'Clothing'),
        ('Transportation', 'Transportation'),
        ('Home', 'Home'),
        ('Bills', 'Bills '),
        ('Entertainment', 'Entertainment'),
        ('Household_goods', 'Household Goods'),
        ('personnel_needs', 'Personnel Needs'),
        ('Education', 'Education'),
        ('Sports', 'Sports'),
        ('Others', 'Others'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_type = models.CharField(max_length=25)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES)
    date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.expense_type

    def get_absolute_url(self):
        return reverse('finance-home')


class Income(models.Model):
    INCOME_CHOICES = [
        ('Salary', 'Salary'),
        ('Sales', 'Sales'),
        ('Dividends', 'Dividends'),
        ('Rental', 'Rental'),
        ('Grants', 'Grants'),
        ('Refunds', 'Refunds'),
        ('Awards', 'Awards'),
        ('Others', 'Others'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income_type = models.CharField(max_length=25)
    category = models.CharField(max_length=25, choices=INCOME_CHOICES)
    date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.income_type

    def get_absolute_url(self):
        return reverse('finance-home')


"""class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget_limit = models.IntegerField(default=25000)

    def save(self, *args, **kwargs):
        super(Budget, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user} budget_limit'"""
