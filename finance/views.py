from django.shortcuts import render
# from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ExpenseForm
from .models import Expense
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

"""@login_required
def home(request):
    context = request.user.expense_set.all()
    return render(request, 'finance/home.html', {"title": "Home page", 'expenses': context})"""


class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'finance/home.html'
    context_object_name = 'expenses'
    paginate_by = 25

    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user).order_by('-date')


class ExpenseDetailView(DetailView):
    model = Expense


class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    model = Expense
    fields = ['expense_type', 'amount', 'category', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseDeleteView(DeleteView):
    model = Expense
    success_url = '/'


@login_required
def about(request):
    return render(request, 'finance/about.html')
