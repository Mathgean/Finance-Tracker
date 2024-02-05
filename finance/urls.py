from django.urls import path
from . import views
from .views import ExpenseDetailView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView, ExpenseListView

urlpatterns = [
    path('', ExpenseListView.as_view(), name='finance-home'),
    path('expense/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('expense/add/', ExpenseCreateView.as_view(), name='expense-create'),
    path('expense/<int:pk>/update/', ExpenseUpdateView.as_view(), name='expense-update'),
    path('expense/<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense-delete'),
]