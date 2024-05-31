from modeltranslation.translator import TranslationOptions, register
from common import models


@register(models.AboutConfederation)
class AboutConfederationTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(models.AboutGuides)
class AboutGuidesTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(models.AboutDocuments)
class AboutDocumentsTranslationOptions(TranslationOptions):
    fields = ("document",)


@register(models.AboutRegulations)
class AboutRegulationsTranslationOptions(TranslationOptions):
    fields = ("document",)


@register(models.AboutMembership)
class AboutMembershipTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(models.CompetitonCalendars)
class CompetitonCalendarsTranslationOptions(TranslationOptions):
    fields = ("document",)


@register(models.CompetitionReports)
class CompetitionReportsTranslationOptions(TranslationOptions):
    fields = ("document",)


@register(models.CompetitionDocuments)
class CompetitionDocumentsTranslationOptions(TranslationOptions):
    fields = ("document",)


@register(models.KurashHistory)
class KurashHistoryTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(models.KurashRules)
class KurashRulesTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(models.KurashProvisions)
class KurashProvisionsTranslationOptions(TranslationOptions):
    fields = ("document",)


@register(models.EventsAnnouncements)
class EventsAnnouncementsTranslationOptions(TranslationOptions):
    fields = ("content",)
