from django.contrib import admin
from .models import AboutConfederation
from common.mixins import TabbedTranslationAdmin


@admin.register(AboutConfederation)
class AboutConfederationAdmin(TabbedTranslationAdmin):
    # exclude = ("content",)
    pass
