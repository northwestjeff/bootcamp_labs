from django.shortcuts import render
# from pages.models import ClientUser, Organization, Loan, Borrower, Covenants, Portfolio, NoncompliantPortfolio

def home(request):
    # ClientUser = ClientUser.objects.all()
    # organization = Organization.objects.all()
    # portfolio = Portfolio.objects.all()
    return render(request, 'pages/home.html', {})

# Create your views here.
