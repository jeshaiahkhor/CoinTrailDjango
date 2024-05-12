from django.urls import path

from . import views

app_name = "expense_track"
urlpatterns = [
    # ex: /expense_track/
    path("transactions/", views.index, name="index"),
    # ex: /expense_track/5/details
    path("transactions/<int:transaction_id>/", views.details, name="details"),
    # ex: /expense_track/summary
    path("summary/", views.summary, name="summary"),
    # ex: /expense_track/test
    path("test/", views.test, name="test")
]