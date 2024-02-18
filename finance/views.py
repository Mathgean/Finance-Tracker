# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView

from .forms import ExpenseForm, IncomeForm
from .models import Expense, Income


@login_required
def home(request):
    amount_spend = 0
    budget_exceeded = 0
    for i in request.user.expense_set.all():
        amount_spend += i.amount
    amount_spend = request.user.profile.budget_limit - amount_spend
    if amount_spend < 0:
        budget_exceeded = amount_spend * -1
        amount_spend = 0
    context = {"title": "Home page", 'expenses': request.user.expense_set.all(),
               "incomes": request.user.income_set.all(), 'paginate_by': 5, 'remaining_budget': amount_spend,
               'budget_exceeded': budget_exceeded}
    return render(request, 'finance/home.html', context)


"""class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'finance/home.html'
    context_object_name = 'expenses'
    paginate_by = 25

    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user).order_by('-date')"""


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


class IncomeDetailView(DetailView):
    model = Income


class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    form_class = IncomeForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    fields = ['income_type', 'amount', 'category', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IncomeDeleteView(DeleteView):
    model = Income
    success_url = '/'


@login_required
def about(request):
    return render(request, 'finance/about.html')


def expense_chart(request):
    def find_amount(expense, category):
        c_amount = 0
        for i in expense:
            if i.category == category:
                c_amount += i.amount
        return c_amount

    expenses = request.user.expense_set.all()

    food = find_amount(expenses, 'Food')
    clothing = find_amount(expenses, 'Clothing')
    transport = find_amount(expenses, 'Transportation')
    homes = find_amount(expenses, 'Home')
    bills = find_amount(expenses, 'Bills')
    entertainment = find_amount(expenses, 'Entertainment')
    goods = find_amount(expenses, 'Household Goods')
    needs = find_amount(expenses, 'Personnel Needs')
    education = find_amount(expenses, 'Education')
    sports = find_amount(expenses, 'Sports')
    others = find_amount(expenses, 'Others')
    category_name = ['Food', 'Clothing', 'Transportation', 'Home', 'Bills', 'Entertainment', 'Household Goods',
                     'Personnel Needs', 'Education', 'Sports', 'Others']
    category_amount = [food, clothing, transport, homes, bills, entertainment, goods, needs, education, sports, others]
    context = {
        'category_name': category_name,
        'category_amount': category_amount
    }
    return render(request, 'finance/expense_chart.html', context)


def income_chart(request):
    def find_amount(income, category):
        c_amount = 0
        for i in income:
            if i.category == category:
                c_amount += i.amount
        return c_amount

    incomes = request.user.income_set.all()

    salary = find_amount(incomes, 'Salary')
    sales = find_amount(incomes, 'Sales')
    dividends = find_amount(incomes, 'Dividends')
    rental = find_amount(incomes, 'Rental')
    grands = find_amount(incomes, 'Grands')
    refunds = find_amount(incomes, 'Refunds')
    awards = find_amount(incomes, 'Awards')
    others = find_amount(incomes, 'Others')
    category_name = ['Salary', 'Sales', 'Dividends', 'Rental', 'Grands', 'Refunds', 'Awards', 'Others']
    category_amount = [salary, sales, dividends, rental, grands, refunds, awards, others]
    context = {
        'category_name': category_name,
        'category_amount': category_amount
    }
    return render(request, 'finance/income_chart.html', context)
