from django.urls import path
from about import views


urlpatterns = [
    path("confederation/", views.ConfederationTemplateView.as_view()),
    path("guides/", views.GuidesTemplateView.as_view()),
    path("documents/", views.DocumentsTemplateView.as_view()),
    path("regulations/", views.RegulationsTemplateView.as_view()),
    path("symbols/", views.SymbolsTemplateView.as_view()),
    path("membership/", views.MembershipView.as_view()),
]
