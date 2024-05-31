from django.contrib import admin
from common.mixins import TabbedTranslationAdmin
from common import models


# @admin.register(models.Regulations)
# class RegulationsAdmin(TabbedTranslationAdmin):
#     pass


# @admin.register(models.CompetitionReports)
# class CompetitionReportsAdmin(TabbedTranslationAdmin):
#     pass


# @admin.register(models.CompetitionDocuments)
# class CompetitionDocumentsAdmin(TabbedTranslationAdmin):
#     pass


# admin.site.register(models.CarouselImage)
# admin.site.register(models.GalleryImage)


# @admin.register(models.Confederation)
# class ConfederationAdmin(TabbedTranslationAdmin):
#     pass


# @admin.register(models.Guides)
# class GuidesAdmin(TabbedTranslationAdmin):
#     pass


# @admin.register(models.Membership)
# class MembershipAdmin(TabbedTranslationAdmin):
#     pass


# @admin.register(models.Symbols)
# class SymbolsAdmin(TabbedTranslationAdmin):
#     pass


# @admin.register(models.History)
# class HistoryAdmin(TabbedTranslationAdmin):
#     pass


# @admin.register(models.Rules)
# class RulesAdmin(TabbedTranslationAdmin):
#     pass


########################################################3


@admin.register(models.Documents)
class DocumentsAdmin(TabbedTranslationAdmin):
    list_display = ("id", "title", "document_type")
