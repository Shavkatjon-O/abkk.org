import os

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Confederation(BaseModel):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Confederation"
        verbose_name_plural = "Confederation"

    def __str__(self):
        return self.title or str(self.id)


class Guides(BaseModel):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Guides"
        verbose_name_plural = "Guides"

    def __str__(self):
        return self.title or str(self.id)


class Membership(BaseModel):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Membership"

    def __str__(self):
        return self.title or str(self.id)


class Symbols(BaseModel):
    title = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Symbols"
        verbose_name_plural = "Symbols"

    def __str__(self):
        return self.title or str(self.id)


class Documents(BaseModel):
    title = models.CharField(max_length=256)
    pdf = models.FileField(upload_to="documents/", null=True, blank=True)
    file_name = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        verbose_name = "Documents"
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.title or str(self.id)


class Regulations(BaseModel):
    title = models.CharField(max_length=256)
    pdf = models.FileField(upload_to="documents/", null=True, blank=True)
    file_name = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        verbose_name = "Regulations"
        verbose_name_plural = "Regulations"

    def __str__(self):
        return self.title or str(self.id)
