from django.urls import path
from common import views

urlpatterns = [
    path(
        "",
        views.HomePageView.as_view(),
        name="home_page",
    ),
    path(
        "about/confederation/",
        views.AboutConfederationView.as_view(),
        name="about_confederation",
    ),
    path(
        "about/guides/",
        views.AboutGuidesView.as_view(),
        name="about_guides",
    ),
    path(
        "about/documents/",
        views.AboutDocumentsView.as_view(),
        name="about_documents",
    ),
    path(
        "about/regulations/",
        views.AboutRegulationsView.as_view(),
        name="about_regulations",
    ),
    path(
        "about/symbols/",
        views.AboutSymbolsView.as_view(),
        name="about_symbols",
    ),
    path(
        "about/membership/",
        views.AboutMembershipView.as_view(),
        name="about_membership",
    ),
    path(
        "kurash/history/",
        views.KurashHistoryView.as_view(),
        name="kurash_history",
    ),
    path(
        "kurash/rules/",
        views.KurashRulesView.as_view(),
        name="kurash_rules",
    ),
    path(
        "competition/reports/",
        views.CompetitionReportsView.as_view(),
        name="competition_reports",
    ),
    path(
        "competition/documents/",
        views.CompetitionDocumentsView.as_view(),
        name="competition_documents",
    ),
]
