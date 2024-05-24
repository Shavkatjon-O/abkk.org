from django.views.generic import TemplateView
from . import models


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


class RegulationsView(TemplateView):
    template_name = "about/regulations.html"


class SymbolsView(TemplateView):
    template_name = "about/symbols.html"


class MembershipView(TemplateView):
    template_name = "about/membership.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["membership"] = models.AboutMembership.objects.first()
        return context
