from django.db import models
from django import forms
from django.contrib.auth.models import User
from localflavor.us.models import USStateField
from djmoney.models.fields import MoneyField

class Loan(models.Model):
    loan_id = models.CharField(max_length=15, blank=True, null=True)
    business_name = models.CharField(max_length=15, blank=True, null=True)
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    origination_date = models.DateField()
    maturity_date = models.DateField()
    payment_schedule_options = (
        ('WEEKLY', 'weekly'),
        ('MONTHLY', 'monthly'),
        ('QUARTERLY', 'quarterly'),
        ('SEMI-ANNUALLY', 'semi-annually'),
        ('ANNUALLY', 'annually')
    )
    payment_schedule = forms.ChoiceField(choices=payment_schedule_options)
    regular_payment_amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    loan_compliance = models.BooleanField(default=True)  # If all covenants are true
    portfolio = models.ForeignKey('Portfolio', related_name='loans')
    noncomp_portfolio = models.ForeignKey('NoncompliantPortfolio', related_name='loans')
    borrower = models.ForeignKey('Borrower', related_name='loans')

    def __str__(self):
        return self.loan_id, self.business_name, self.amount


class Covenants(models.Model):
    cov_id = models.CharField(max_length=15, default="Covenant ID")
    indicator_options = (
        ('DSCR', 'Debt Service Coverage Ratio'),
        ('TOTAL_LIABILITIES', 'Total Liabilities'),
        ('CURRENT_RATIO', 'Current Ratio'),
    )
    indicator = forms.ChoiceField(choices=indicator_options)
    operator_options = (
        ('GREATER_THAN', '>'),
        ('LESS_THAN', '<'),
        ('EQUAL_TO', '='),
        ('NOT_EQUAL_TO', '≠'),
    )
    operator_options = forms.ChoiceField(choices=operator_options)
    standard = models.IntegerField(default=0)
    compliance = models.BooleanField(default=True)
    date_last_compliant = models.DateField()
    num_times_noncomp = models.PositiveSmallIntegerField(default=0)
    loans = models.ForeignKey(Loan, related_name='covenants')

    def __str__(self):
        return self.cov_id, self.indicator




class Portfolio(models.Model):
    total_origination = models.FloatField(default=0)

    def add_function(self):
        self.total_origination = 0
        loans = self.loans.all()
        for i in loans:
            self.total_origination += i.amount

    def __str__(self):
        return self.loans  # , self.total_origination


class ClientUser(models.Model):
    username = models.CharField(max_length=15, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username


class Organization(models.Model):
    business_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = USStateField(null=True, blank=True)
    zip = models.CharField(max_length=5, blank=True, null=True)
    portfolio = models.OneToOneField('Portfolio')

    def __str__(self):
        return self.business_name


class Borrower(models.Model):
    # Need to inherit from Organization class
    compliance = models.BooleanField(default=True)  # If all loans compliance === true


class NoncompliantPortfolio(models.Model):
    total_origination = models.FloatField(default=0)

    def add_function(self):
        self.total_origination = 0
        loans = self.loans.all()
        for i in loans:
            self.total_origination += i.amount

    def __str__(self):
        return self.loans, self.total_origination
