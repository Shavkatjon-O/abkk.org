from modeltranslation.translator import TranslationOptions, register
from .models import AboutConfederation


@register(AboutConfederation)
class AboutConfederationTranslationOptions(TranslationOptions):
    fields = ("content",)
