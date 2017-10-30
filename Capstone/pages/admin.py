from django.contrib import admin
from pages.models import ClientUser, Organization, Loan, Borrower, Covenants, Portfolio, NoncompliantPortfolio


admin.site.register(ClientUser)
admin.site.register(Organization)
admin.site.register(Loan)
admin.site.register(Borrower)
admin.site.register(Portfolio)
admin.site.register(Covenants)
admin.site.register(NoncompliantPortfolio)

# Register your models here.
