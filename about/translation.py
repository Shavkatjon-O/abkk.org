from modeltranslation.translator import TranslationOptions, register
from . import models


@register(models.AboutConfederation)
class AboutConfederationTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.AboutGuides)
class AboutGuidesTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.AboutMembership)
class AboutMembershipTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.AboutSymbols)
class AboutSymbolsTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.AboutDocuments)
class AboutDocumentsTranslationOptions(TranslationOptions):
    fields = ("title", "pdf")


@register(models.AboutRegulations)
class AboutRegulationsTranslationOptions(TranslationOptions):
    fields = ("title", "pdf")
