from modeltranslation.translator import TranslationOptions, register
from apps.common import models


@register(models.AboutConfederation)
class AboutConfederationTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(models.AboutGuides)
class AboutGuidesTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(models.AboutDocuments)
class AboutDocumentsTranslationOptions(TranslationOptions):
    fields = ("title", "document")


@register(models.AboutRegulations)
class AboutRegulationsTranslationOptions(TranslationOptions):
    fields = ("title", "document")


@register(models.AboutMembership)
class AboutMembershipTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(models.CompetitonCalendars)
class CompetitonCalendarsTranslationOptions(TranslationOptions):
    fields = ("title", "document")


@register(models.CompetitionReports)
class CompetitionReportsTranslationOptions(TranslationOptions):
    fields = ("title", "document")


@register(models.CompetitionDocuments)
class CompetitionDocumentsTranslationOptions(TranslationOptions):
    fields = ("title", "document")


@register(models.KurashHistory)
class KurashHistoryTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(models.KurashRules)
class KurashRulesTranslationOptions(TranslationOptions):
    fields = ("content",)


@register(models.KurashProvisions)
class KurashProvisionsTranslationOptions(TranslationOptions):
    fields = ("title", "document")


@register(models.EventsAnnouncements)
class EventsAnnouncementsTranslationOptions(TranslationOptions):
    fields = ("title", "content")


@register(models.EventsEvents)
class EventsEventsTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ("title",)


@register(models.GalleryPhoto)
class GalleryPhotoTranslationOptions(TranslationOptions):
    fields = ("title",)
