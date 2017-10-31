from django.shortcuts import render
from pages.forms import NewLoanForm, NewCovenantForm

from pages.models import ClientUser, Loan, Covenant  # , Borrower, Organization, Portfolio, NoncompliantPortfolio


def home(request):
    client_user = ClientUser.objects.all()
    # organization = Organization.objects.all()
    loans = Loan.objects.all()
    loans_sum = 0
    for i in loans:
        loans_sum += i.amount
    covenants = Covenant.objects.all()
    return render(request, 'pages/home.html', {"client_user": client_user,
                                               "loans": loans,
                                               "loans_sum": loans_sum,
                                               "covenants": covenants
                                               })


def new_loan(request):
    form = NewLoanForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            loan = form.save(commit=False)
            loan.save()
    return render(request, 'pages/new_loan.html', {"form": form})


def new_covenant(request):
    form = NewCovenantForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            loan = form.save(commit=False)
            loan.save()
    return render(request, 'pages/new_loan.html', {"form": form})
