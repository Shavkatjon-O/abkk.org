from django.urls import path
from common import views

urlpatterns = [
    path(
        "about/confederation/", views.ConfederationView.as_view(), name="confederation"
    ),
    path("about/guides/", views.GuidesView.as_view(), name="guides"),
    path("about/documents/", views.DocumentsView.as_view(), name="documents"),
    path("about/regulations/", views.RegulationsView.as_view(), name="regulations"),
    path("about/symbols/", views.SymbolsView.as_view(), name="symbols"),
    path("about/membership/", views.MembershipView.as_view(), name="membership"),
]
