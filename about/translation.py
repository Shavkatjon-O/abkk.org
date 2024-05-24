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
