from django.views.generic import TemplateView
from about import models


class ConfederationTemplateView(TemplateView):
    template_name = "about/confederation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["common_objects"] = models.Common.objects.first()
        return context


class GuidesTemplateView(TemplateView):
    template_name = "about/guides.html"


class DocumentsTemplateView(TemplateView):
    template_name = "about/documents.html"


class RegulationsTemplateView(TemplateView):
    template_name = "about/regulations.html"


class SymbolsTemplateView(TemplateView):
    template_name = "about/symbols.html"


class MembershipView(TemplateView):
    template_name = "about/membership.html"
