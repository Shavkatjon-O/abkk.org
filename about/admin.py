from django.contrib import admin
from common.mixins import TabbedTranslationAdmin
from . import models


@admin.register(models.AboutConfederation)
class AboutConfederationAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.AboutGuides)
class AboutGuidesAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.AboutMembership)
class AboutMembershipAdmin(TabbedTranslationAdmin):
    pass
