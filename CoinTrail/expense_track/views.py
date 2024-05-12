# from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Transaction


# Shows an index of the most recent 5 transactions.
def index(request):
    latest_transaction_list = Transaction.objects.order_by("-date")[:5]
    context = {"latest_transaction_list": latest_transaction_list}
    return render(request, "expense_track/index.html", context)


# Shows the expanded details of a single transaction.
def details(request, transaction_id):
    selected_transaction = get_object_or_404(Transaction, pk=transaction_id)
    return render(request, "expense_track/details.html",
                  {"transaction": selected_transaction.details}, content_type="text/plain")


def summary(request):
    full_transaction_list = Transaction.objects.sort_income_accounts("MAE")
    return HttpResponse(full_transaction_list)


def test(request):
    return render(request, "expense_track/test.html",
                  {"income_accounts": Transaction.objects.get_income_accounts()})