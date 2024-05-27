from modeltranslation.translator import TranslationOptions, register
from common import models


@register(models.Confederation)
class ConfederationTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.Guides)
class GuidesTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.Membership)
class MembershipTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.Symbols)
class SymbolsTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.Documents)
class DocumentsTranslationOptions(TranslationOptions):
    fields = ("title", "pdf", "file_name")


@register(models.Regulations)
class RegulationsTranslationOptions(TranslationOptions):
    fields = ("title", "pdf", "file_name")


@register(models.History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.Rules)
class RulesTranslationOptions(TranslationOptions):
    fields = ("title", "content")
