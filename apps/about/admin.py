from django.contrib import admin

from apps.common.mixins import TabbedTranslationAdmin
from apps.about import models


@admin.register(models.Confederation)
class ConfederationAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.Management)
class ManagementAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.ConstituentDocuments)
class ConstituentDocumentsAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.Charter)
class CharterAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.Membership)
class MembershipAdmin(TabbedTranslationAdmin):
    pass
