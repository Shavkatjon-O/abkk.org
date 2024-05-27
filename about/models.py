from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class AboutConfederation(models.Model):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Confederation"
        verbose_name_plural = "Confederation"

    def __str__(self):
        return self.title or str(self.id)


class AboutGuides(models.Model):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Guides"
        verbose_name_plural = "Guides"

    def __str__(self):
        return self.title or str(self.id)


class AboutMembership(models.Model):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Membership"
        verbose_name_plural = "Membership"

    def __str__(self):
        return self.title or str(self.id)


class AboutSymbols(models.Model):
    title = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Symbols"
        verbose_name_plural = "Symbols"

    def __str__(self):
        return self.title or str(self.id)


class AboutDocuments(models.Model):
    title = models.CharField(max_length=256)
    pdf = models.FileField(upload_to="documents/", null=True, blank=True)

    class Meta:
        verbose_name = "Documents"
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.title or str(self.id)


class AboutRegulations(models.Model):
    title = models.CharField(max_length=256)
    pdf = models.FileField(upload_to="documents/", null=True, blank=True)

    class Meta:
        verbose_name = "Regulations"
        verbose_name_plural = "Regulations"

    def __str__(self):
        return self.title or str(self.id)
