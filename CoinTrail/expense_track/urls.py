from django.urls import path

from . import views

urlpatterns = [
    # ex: /expense_track/
    path("", views.index, name="index"),
    # ex: /expense_track/5/details
    path("<int:transaction_id>/", views.details, name="details"),
]