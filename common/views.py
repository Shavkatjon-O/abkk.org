from django.shortcuts import render
from django.views.generic import TemplateView
from common import models


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["announcement"] = models.EventsAnnouncements.objects.first()
        context["carousel"] = models.Carousel.objects.all()
        context["gallery"] = models.Gallery.objects.all().order_by("-id")[:3]

        return context


class AboutConfederationView(TemplateView):
    template_name = "about_confederation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["confederation"] = models.AboutConfederation.objects.first()

        return context


class AboutGuidesView(TemplateView):
    template_name = "about_guides.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["guides"] = models.AboutGuides.objects.first()

        return context


class AboutDocumentsView(TemplateView):
    template_name = "about_documents.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.AboutDocuments.objects.all()

        return context


class AboutRegulationsView(TemplateView):
    template_name = "about_regulations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.AboutRegulations.objects.all()

        return context


class AboutSymbolsView(TemplateView):
    template_name = "about_symbols.html"


class AboutMembershipView(TemplateView):
    template_name = "about_membership.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["membership"] = models.AboutMembership.objects.first()

        return context


class CompetitonCalendarsView(TemplateView):
    template_name = "competition_calendars.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.CompetitonCalendars.objects.all()

        return context


class CompetitionReportsView(TemplateView):
    template_name = "competition_reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.CompetitionReports.objects.all()

        return context


class CompetitionDocumentsView(TemplateView):
    template_name = "competition_documents.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.CompetitionDocuments.objects.all()

        return context


class KurashHistoryView(TemplateView):
    template_name = "kurash_history.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["history"] = models.KurashHistory.objects.first()
        return context


class KurashRulesView(TemplateView):
    template_name = "kurash_rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rules"] = models.KurashRules.objects.first()
        return context


class KurashProvisionsView(TemplateView):
    template_name = "kurash_provisions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.KurashProvisions.objects.all()

        return context


class EventsAnnouncementsView(TemplateView):
    template_name = "events_announcements.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["announcements"] = models.EventsAnnouncements.objects.all()

        return context


class EventsAboutUsView(TemplateView):
    template_name = "events_about_us.html"
