from django.shortcuts import render
from django.views.generic import TemplateView

from . import models


def home_page(request):
    return render(request, "home.html")


class ConfederationView(TemplateView):
    template_name = "about/confederation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["confederation"] = models.AboutConfederation.objects.first()
        return context


class GuidesView(TemplateView):
    template_name = "about/guides.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["guides"] = models.AboutGuides.objects.first()
        return context


class DocumentsView(TemplateView):
    template_name = "about/documents.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.AboutDocuments.objects.first()
        return context


class RegulationsView(TemplateView):
    template_name = "about/regulations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["regulations"] = models.AboutRegulations.objects.first()
        return context


class SymbolsView(TemplateView):
    template_name = "about/symbols.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["symbols"] = models.AboutSymbols.objects.first()
        return context


class MembershipView(TemplateView):
    template_name = "about/membership.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["membership"] = models.AboutMembership.objects.first()
        return context
