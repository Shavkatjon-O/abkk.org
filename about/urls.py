from django.urls import path
from . import views

urlpatterns = [
    path("confederation/", views.ConfederationView.as_view(), name="confederation"),
    path("guides/", views.GuidesView.as_view(), name="guides"),
    path("documents/", views.DocumentsView.as_view(), name="documents"),
    path("regulations/", views.RegulationsView.as_view(), name="regulations"),
    path("symbols/", views.SymbolsView.as_view(), name="symbols"),
    path("membership/", views.MembershipView.as_view(), name="membership"),
]
