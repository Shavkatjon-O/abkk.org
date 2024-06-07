from modeltranslation.translator import TranslationOptions, register
from apps.common import models


@register(models.Confederation)
class ConfederationTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(models.Management)
class ManagementTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(models.ConstituentDocuments)
class ConstituentDocumentsTranslationOptions(TranslationOptions):
    fields = ("title", "document")


@register(models.Charter)
class CharterTranslationOptions(TranslationOptions):
    fields = ("title", "document")


@register(models.Membership)
class MembershipTranslationOptions(TranslationOptions):
    fields = ("content",)
