from django.db import models
from django import forms
from django.contrib.auth.models import User


class ClientUser(models.Model):
    username = "username"
    first_name = "firstname"
    last_name = "lastname"


    def __str__(self):
        return self.username

class Organization(models.Model):
    business_name = "business name"
    address = "number and street"
    city = "city"
    state = "state"
    zip = "number"
    portfolio = "connect to class Portfolio"

    def __str__(self):
        return self.business_name

class Borrower(models.Model):
    # Need to inherit from Organization class
    loans = "array of loan_id"


class Loan(models.Model):
    loan_id = "number"
    borrower = "business"
    amount = "number"
    origination_date = "date"
    maturity_date = "date"
    covenants = "list of covenants"
    payment_schedule = "weekly, monthly, quarterly, semi-annually, yearly"
    regular_payment_amount = "amount"
    loan_compliance = True

    def __str__(self):
        return self.loan_id, self.borrower, self.amount

class Covenants(models.Model):
    cov_id = "number"
    str = "DSCR greater than 1.25"
    indicator = "Key Ratio"
    operator = "list of greater than, less than, equal to, not equal to"
    standard = "number"
    compliance = True
    date_last_compliant = "date"
    num_times_noncomp = "NC counter"

    def __str__(self):
        return self.cov_id, self.indicator

class Portfolio(models.Model):
    loans = "array of loans"
    total_origination = "sum of loans value"

    def __str__(self):
        return self.loans, self.total_origination

class NoncompliantPortfolio(models.Model):
    loans = "array of NC loans"
    total_origination = "sum of loans value"

    def __str__(self):
        return self.loans, self.total_origination
