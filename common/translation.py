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


# @register(models.Confederation)
# class ConfederationTranslationOptions(TranslationOptions):
#     fields = ("title", "content")


# @register(models.Guides)
# class GuidesTranslationOptions(TranslationOptions):
#     fields = ("title", "content")


# @register(models.Membership)
# class MembershipTranslationOptions(TranslationOptions):
#     fields = ("title", "content")


# @register(models.Symbols)
# class SymbolsTranslationOptions(TranslationOptions):
#     fields = ("title",)


# @register(models.Documents)
# class DocumentsTranslationOptions(TranslationOptions):
#     fields = ("title", "document")


# @register(models.Regulations)
# class RegulationsTranslationOptions(TranslationOptions):
#     fields = ("title", "document")


# @register(models.CompetitionReports)
# class CompetitionReportsTranslationOptions(TranslationOptions):
#     fields = ("title", "document")


# @register(models.CompetitionDocuments)
# class CompetitionDocumentsTranslationOptions(TranslationOptions):
#     fields = ("title", "document")


# @register(models.History)
# class HistoryTranslationOptions(TranslationOptions):
#     fields = ("title", "content")


# @register(models.Rules)
# class RulesTranslationOptions(TranslationOptions):
#     fields = ("title", "content")
