import os

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class DocumentsChoices(models.TextChoices):
    CONSTITUENT = "CONSTITUENT", "Учредительные"
    REGULATIONS = "REGULATIONS", "Устав"
    PROVISIONS = "PROVISIONS", "Положения"
    REPORTS = "REPORTS", "Протоколы"
    DOCUMENTS = "DOCUMENTS", "Документы"


class Documents(BaseModel):
    title = models.CharField(max_length=256, verbose_name="Название файла")

    document_type = models.CharField(
        max_length=256, choices=DocumentsChoices.choices, verbose_name="Тип документа"
    )
    document = models.FileField(upload_to="documents/", verbose_name="Документ")

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title


########################################################################


class CarouselImage(BaseModel):
    image = models.ImageField(upload_to="carousel/")

    def __str__(self):
        return self.image.name


class GalleryImage(BaseModel):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="gallery/")
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


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


class Temp(BaseModel):
    title = models.CharField(max_length=256, null=True, blank=True)
    document = models.FileField(upload_to="documents/", null=True, blank=True)

    class Meta:
        verbose_name = "Documents"
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.title or str(self.id)


class Regulations(BaseModel):
    title = models.CharField(max_length=256, null=True, blank=True)
    document = models.FileField(upload_to="documents/", null=True, blank=True)

    class Meta:
        verbose_name = "Regulations"
        verbose_name_plural = "Regulations"

    def __str__(self):
        return self.title or str(self.id)


class CompetitionReports(BaseModel):
    title = models.CharField(max_length=256, null=True, blank=True)
    document = models.FileField(upload_to="documents/", null=True, blank=True)

    class Meta:
        verbose_name = "Competition Reports"
        verbose_name_plural = "Competition Reports"

    def __str__(self):
        return self.title or str(self.id)


class CompetitionDocuments(BaseModel):
    title = models.CharField(max_length=256, null=True, blank=True)
    document = models.FileField(upload_to="documents/", null=True, blank=True)

    class Meta:
        verbose_name = "Competition Documents"
        verbose_name_plural = "Competition Documents"

    def __str__(self):
        return self.title or str(self.id)


class History(BaseModel):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "History"
        verbose_name_plural = "History"

    def __str__(self):
        return self.title or str(self.id)


class Rules(BaseModel):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Rules"
        verbose_name_plural = "Rules"

    def __str__(self):
        return self.title or str(self.id)
