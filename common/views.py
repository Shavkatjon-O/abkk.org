from django.shortcuts import render
from django.views.generic import TemplateView
from common import models


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carousel"] = models.CarouselImage.objects.all()
        context["gallery"] = models.GalleryImage.objects.all()
        return context


class ConfederationView(TemplateView):
    template_name = "about_confederation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["confederation"] = models.Confederation.objects.first()
        return context


class GuidesView(TemplateView):
    template_name = "about_guides.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["guides"] = models.Guides.objects.first()
        return context


class DocumentsView(TemplateView):
    template_name = "about_documents.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.Documents.objects.all()
        return context


class RegulationsView(TemplateView):
    template_name = "about_regulations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["regulations"] = models.Regulations.objects.all()
        return context


class CompetitionReportsView(TemplateView):
    template_name = "competition_reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["competition_reports"] = models.CompetitionReports.objects.all()
        return context


class CompetitionDocumentsView(TemplateView):
    template_name = "competition_documents.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["competition_documents"] = models.CompetitionDocuments.objects.all()
        return context


class SymbolsView(TemplateView):
    template_name = "about_symbols.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["symbols"] = models.Symbols.objects.first()
        return context


class MembershipView(TemplateView):
    template_name = "about_membership.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["membership"] = models.Membership.objects.first()
        return context


class HistoryView(TemplateView):
    template_name = "kurash_history.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["history"] = models.History.objects.first()
        return context


class RulesView(TemplateView):
    template_name = "kurash_rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rules"] = models.Rules.objects.first()
        return context
