from django.contrib import admin
from common.mixins import TabbedTranslationAdmin
from common import models


@admin.register(models.AboutConfederation)
class AboutConfederationAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.AboutGuides)
class AboutGuidesAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.AboutDocuments)
class AboutDocumentsAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.AboutRegulations)
class AboutRegulationsAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.AboutSymbols)
class AboutSymbolsAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.AboutMembership)
class AboutMembershipAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.CompetitonCalendar)
class CompetitonCalendarAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.CompetitionReports)
class CompetitionReportsAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.CompetitionDocuments)
class CompetitionDocumentsAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.KurashHistory)
class KurashHistoryAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.KurashRules)
class KurashRulesAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.KurashProvisions)
class KurashProvisionsAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.EventsAnnouncements)
class EventsAnnouncementsAdmin(TabbedTranslationAdmin):
    pass


admin.site.register(models.Carousel)
admin.site.register(models.Gallery)
