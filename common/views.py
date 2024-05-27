from django.shortcuts import render
from django.views.generic import TemplateView
from common import models


class HomePageView(TemplateView):
    template_name = "home.html"


class ConfederationView(TemplateView):
    template_name = "confederation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["confederation"] = models.Confederation.objects.first()
        return context


class GuidesView(TemplateView):
    template_name = "guides.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["guides"] = models.Guides.objects.first()
        return context


class DocumentsView(TemplateView):
    template_name = "documents.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.Documents.objects.first()
        return context


class RegulationsView(TemplateView):
    template_name = "regulations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["regulations"] = models.Regulations.objects.first()
        return context


class SymbolsView(TemplateView):
    template_name = "symbols.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["symbols"] = models.Symbols.objects.first()
        return context


class MembershipView(TemplateView):
    template_name = "membership.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["membership"] = models.Membership.objects.first()
        return context
