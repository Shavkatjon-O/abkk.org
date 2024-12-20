from django.urls import path
from apps.common import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home_page"),
    path(
        "about/confederation/",
        views.AboutConfederationView.as_view(),
        name="about_confederation",
    ),
    path("about/guides/", views.AboutGuidesView.as_view(), name="about_guides"),
    path(
        "about/documents/", views.AboutDocumentsView.as_view(), name="about_documents"
    ),
    path(
        "about/regulations/",
        views.AboutRegulationsView.as_view(),
        name="about_regulations",
    ),
    path("about/symbols/", views.AboutSymbolsView.as_view(), name="about_symbols"),
    path(
        "about/membership/",
        views.AboutMembershipView.as_view(),
        name="about_membership",
    ),
    path("kurash/history/", views.KurashHistoryView.as_view(), name="kurash_history"),
    path("kurash/rules/", views.KurashRulesView.as_view(), name="kurash_rules"),
    path(
        "kurash/provisions/",
        views.KurashProvisionsView.as_view(),
        name="kurash_provisions",
    ),
    path(
        "competition/calendars/",
        views.CompetitonCalendarsView.as_view(),
        name="competition_calendars",
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
    path(
        "events/announcements/",
        views.EventsAnnouncementsListView.as_view(),
        name="events_announcements",
    ),
    path(
        "events/announcements/<int:pk>/",
        views.EventsAnnouncementsDetailView.as_view(),
        name="events_announcements_detail",
    ),
    path("events/events/", views.EventsEventsListView.as_view(), name="events_events"),
    path("events/about_us/", views.EventsAboutUsView.as_view(), name="events_about_us"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("gallery/photo/", views.GalleryPhotoListView.as_view(), name="gallery_photo"),
    path("gallery/video/", views.GalleryVideoListView.as_view(), name="gallery_video"),
]
