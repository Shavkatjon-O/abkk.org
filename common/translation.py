from modeltranslation.translator import TranslationOptions, register
from common import models


@register(models.AboutConfederation)
class AboutConfederationTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.AboutGuides)
class AboutGuidesTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.AboutDocuments)
class AboutDocumentsTranslationOptions(TranslationOptions):
    fields = ("title", "document")


@register(models.AboutRegulations)
class AboutRegulationsTranslationOptions(TranslationOptions):
    fields = ("title", "document")


@register(models.AboutSymbols)
class AboutSymbolsTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.AboutMembership)
class AboutMembershipTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.CompetitionReports)
class CompetitionReportsTranslationOptions(TranslationOptions):
    fields = ("title", "document")


@register(models.CompetitionDocuments)
class CompetitionDocumentsTranslationOptions(TranslationOptions):
    fields = ("title", "document")


@register(models.KurashHistory)
class KurashHistoryTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.KurashRules)
class KurashRulesTranslationOptions(TranslationOptions):
    fields = ("title", "content")
