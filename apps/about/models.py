from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField
from apps.common.models import BaseModel


class Confederation(BaseModel):
    content = RichTextUploadingField()

    class Meta:
        verbose_name = _("confederation")
        verbose_name_plural = _("confederation")


class Management(BaseModel):
    content = RichTextUploadingField()

    class Meta:
        verbose_name = _("management")
        verbose_name_plural = _("management")


class ConstituentDocuments(BaseModel):
    title = models.CharField(max_length=256)
    document = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = _("constituent documents")
        verbose_name_plural = _("constituent documents")


class Charter(BaseModel):
    title = models.CharField(max_length=256)
    document = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = _("charter")
        verbose_name_plural = _("charter")


class Membership(BaseModel):
    content = RichTextUploadingField()

    class Meta:
        verbose_name = _("membership")
        verbose_name_plural = _("membership")
