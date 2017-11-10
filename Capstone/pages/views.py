from django.shortcuts import render
from django.http import JsonResponse
from pages.forms import NewLoanForm, NewCovenantForm

from pages.models import ClientUser, Loan, Covenant, Statement, \
    Organization  # , Borrower, Portfolio, NoncompliantPortfolio


def home(request):
    client_user = ClientUser.objects.all()
    # organization = Organization.objects.all()
    loans = Loan.objects.all()
    loans_sum = 0
    temp_list = []
    for i in loans:
        temp_list.append(float(i.amount))
    for i in loans:
        loans_sum += i.amount
    covenants = Covenant.objects.all()
    loan_comp_check(loans)
    return render(request, 'pages/home.html', {"client_user": client_user,
                                               "loans": loans,
                                               "loans_sum": loans_sum,
                                               "covenants": covenants,
                                               "temp_list": temp_list
                                               })
#
def loan_comp_check(loans):
    for i in loans:
        for x in i.covenants.all():
            if x.compliance:
                pass
            else:
                i.loan_compliance = False

#

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


def display(request):
    return render(request, 'pages/display.html', {"statement": Statement.objects.all()})


def organization(request, slug):
    this_slug = slug
    org = Organization.objects.get(slug=this_slug)
    return render(request, 'pages/organization.html', {"organization": org})


def all_organization(request):
    all_org = Organization.objects.all()
    return render(request, 'pages/org.html', {"organization": all_org})


def covenant(request, slug):
    this_slug = slug
    cov = Covenant.objects.get(slug=this_slug)
    cov_val = ""
    if cov.comparison:
        for i in cov.loans.organization.statements.all()[0].data.all():
            if i.column_headers == cov.comparison:
                cov_val = float(i.value)
    if cov.operator_options == "Greater Than" and cov_val > cov.standard:
        cov.compliance = True
    elif cov.operator_options == "Less Than" and cov_val < cov.standard:
        cov.compliance = True
    elif cov.operator_options == "Equal to" and cov_val == cov.standard:
        cov.compliance = True
    elif cov.operator_options == "NOT Equal to" and cov_val != cov.standard:
        cov.compliance = True
    else:
        cov.compliance = False
    cov.save()
    return render(request, 'pages/cov.html', {"covenant": cov,
                                              "values": cov_val
                                              })



def all_covenant(request):
    all_cov = Covenant.objects.all()
    return render(request, 'pages/covenants.html', {"covenant": all_cov})


def all_loans(request):
    loans = Loan.objects.all()
    return render(request, 'pages/loans.html', {"loans": loans})


def view_loan(request, slug):
    this_slug = slug
    a_loan = Loan.objects.get(slug=this_slug)
    return render(request, 'pages/view_loan.html', {"loans": a_loan})


def checkthing(request, id):
    if request.method == 'POST':
        cov = Covenant.objects.get(cov_id=id)
        cov.comparison = request.POST.get('check')
        cov.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'fail'})

# def thing_value(request, list, key):
#     for i in list:
#
#
