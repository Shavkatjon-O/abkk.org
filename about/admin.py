from django.contrib import admin
from .models import AboutConfederation


@admin.register(AboutConfederation)
class AboutConfederationAdmin(admin.ModelAdmin):
    exclude = ("content",)
