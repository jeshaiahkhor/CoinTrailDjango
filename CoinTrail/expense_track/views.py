# from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from .models import Transaction


def index(request):
    latest_transaction_list = Transaction.objects.order_by("-date")[:5]
    context = {"latest_transaction_list": latest_transaction_list}
    return render(request, "expense_track/index.html", context)


def details(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    return render(request, "expense_track/details.html",
                  {"transaction": transaction.details()}, content_type="text/plain")
# Create your views here.
