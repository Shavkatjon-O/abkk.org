from django.views.generic import TemplateView


class ConfederationTemplateView(TemplateView):
    template_name = "about/confederation.html"


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
