from django.urls import path
from about import views


urlpatterns = [
    path(
        "confederation/",
        views.ConfederationTemplateView.as_view(),
        name="confederation",
    ),
    path("guides/", views.GuidesTemplateView.as_view(), name="guides"),
    path("documents/", views.DocumentsTemplateView.as_view(), name="documents"),
    path("regulations/", views.RegulationsTemplateView.as_view(), name="regulations"),
    path("symbols/", views.SymbolsTemplateView.as_view(), name="symbols"),
    path("membership/", views.MembershipView.as_view(), name="membership"),
]
