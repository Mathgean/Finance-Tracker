from django.urls import path
from . import views
from .views import ExpenseDetailView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView, IncomeDetailView, IncomeCreateView, IncomeDeleteView, IncomeUpdateView

urlpatterns = [
    path('', views.home, name='finance-home'),
    path('expense_chart/', views.expense_chart, name='expense-chart'),
    path('income_chart/', views.income_chart, name='income-chart'),
    path('expense/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('expense/add/', ExpenseCreateView.as_view(), name='expense-create'),
    path('expense/<int:pk>/update/', ExpenseUpdateView.as_view(), name='expense-update'),
    path('expense/<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense-delete'),
    path('income/<int:pk>/', IncomeDetailView.as_view(), name='income-detail'),
    path('income/add/', IncomeCreateView.as_view(), name='income-create'),
    path('income/<int:pk>/update/', IncomeUpdateView.as_view(), name='income-update'),
    path('income/<int:pk>/delete/', IncomeDeleteView.as_view(), name='income-delete'),
]