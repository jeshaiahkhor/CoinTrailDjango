from django.urls import path

from . import views

urlpatterns = [
    # ex: /expense_track/
    path("transactions/", views.index, name="index"),
    # ex: /expense_track/5/details
    path("transactions/<int:transaction_id>/", views.details, name="details"),
    # ex: /expense_track/summary
    path("summary/", views.summary, name="summary")
]