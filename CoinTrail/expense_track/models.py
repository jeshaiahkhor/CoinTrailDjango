# Importing libraries
from decimal import Decimal
from datetime import date
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.db.models import Sum


# Creates a model manager for transactions
class TransactionManager(models.Manager):
    # Gets the total expenses incurred to date
    def sort_income_accounts(self, income_account):
        return self.filter(income_account=income_account).aggregate(expense=Sum("expense", default=0))["expense"]

    # Lists all the income accounts found in the transaction history.
    def get_income_accounts(self):
        all_income_accounts = set(self.values_list('income_account', flat=True))    # set() here removes duplicates.
        return all_income_accounts


# Transaction class to handle new transactions
class Transaction(models.Model):
    date = models.DateTimeField(default=timezone.now, blank=False)
    income_account = models.CharField(blank=False, max_length=100)
    expense = models.DecimalField(
        default=10,
        blank=False,
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(Decimal("0.01")), ]
    )
    income = models.DecimalField(
        default=10,
        blank=False,
        decimal_places=2,
        max_digits=10,
        validators=[MinValueValidator(Decimal("0.01")), ]
    )

    description = models.CharField(blank=True, max_length=200)
    expense_account = models.CharField(blank=False, max_length=100)
    category = models.CharField(blank=True, max_length=100)
    subcategory = models.CharField(blank=True, max_length=100)

    objects = TransactionManager()

    # Returns the total change based on the income & expense values
    def get_total(self):
        total = self.income - self.expense
        return round(total, 2)

    # Provides a detailed description of the transaction
    def details(self):
        output = (
                "Transaction: " + str(self.id)
                + "\nDate: " + self.date.strftime("%d/%m/%Y")
                + "\nIncome account: " + self.income_account
                + "\nExpense: " + str(self.expense)
                + "\nIncome: " + str(self.income)
                + "\nTotal: " + str(self.get_total())
                + "\nDescription: " + self.description
                + "\nExpense account: " + self.expense_account
                + "\nCategory: " + self.category
                + "\nSubcategory: " + self.subcategory
        )
        return output

    # A simplified transaction summary for human identification of a transaction.
    def __str__(self):
        output = (
                "Transaction: " + str(self.id)
                + " | Date: " + self.date.strftime("%d/%m/%Y")
        )
        return output
