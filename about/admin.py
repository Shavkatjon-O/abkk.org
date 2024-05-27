from django.contrib import admin
from common.mixins import TabbedTranslationAdmin
from . import models


@admin.register(models.AboutConfederation)
class AboutConfederationAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.AboutGuides)
class AboutGuidesAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.AboutMembership)
class AboutMembershipAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.AboutSymbols)
class AboutSymbolsAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.AboutDocuments)
class AboutDocumentsAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.AboutRegulations)
class AboutRegulationsAdmin(TabbedTranslationAdmin):
    pass
