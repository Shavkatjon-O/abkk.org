import os

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


# class DocumentsChoices(models.TextChoices):
#     CONSTITUENT = "CONSTITUENT", "Учредительные"
#     REGULATIONS = "REGULATIONS", "Устав"
#     PROVISIONS = "PROVISIONS", "Положения"
#     REPORTS = "REPORTS", "Протоколы"
#     DOCUMENTS = "DOCUMENTS", "Документы"


# class Documents(BaseModel):
#     title = models.CharField(max_length=256, verbose_name="Название файла")

#     document_type = models.CharField(
#         max_length=256, choices=DocumentsChoices.choices, verbose_name="Тип документа"
#     )
#     document = models.FileField(upload_to="documents/", verbose_name="Документ")

#     class Meta:
#         verbose_name = "Документ"
#         verbose_name_plural = "Документы"

#     def __str__(self):
#         return self.title


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


class AboutConfederation(BaseModel):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Конфедерация"
        verbose_name_plural = "Конфедерация"

    def __str__(self):
        return self.title


class AboutGuides(BaseModel):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Руководство"
        verbose_name_plural = "Руководство"

    def __str__(self):
        return self.title


class AboutDocuments(BaseModel):
    title = models.CharField(max_length=256)
    document = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = "Учредительные документы"
        verbose_name_plural = "Учредительные документы"

    def __str__(self):
        return self.title


class AboutRegulations(BaseModel):
    title = models.CharField(max_length=256)
    document = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = "Устав"
        verbose_name_plural = "Устав"

    def __str__(self):
        return self.title


class AboutSymbols(BaseModel):
    title = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Символы конфедерации"
        verbose_name_plural = "Символы конфедерации"

    def __str__(self):
        return self.title


class AboutMembership(BaseModel):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Членство в конфедерации"
        verbose_name_plural = "Членство в конфедерации"

    def __str__(self):
        return self.title


class CompetitionReports(BaseModel):
    title = models.CharField(max_length=256)
    document = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = "Протоколы соревнований"
        verbose_name_plural = "Документы о соревнованиях"

    def __str__(self):
        return self.title


class CompetitionDocuments(BaseModel):
    title = models.CharField(max_length=256)
    document = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = "Competition Documents"
        verbose_name_plural = "Competition Documents"

    def __str__(self):
        return self.title


class KurashHistory(BaseModel):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "История белбогли кураш"
        verbose_name_plural = "История белбогли кураш"

    def __str__(self):
        return self.title


class KurashRules(BaseModel):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Правила белбогли кураш"
        verbose_name_plural = "Правила белбогли кураш"

    def __str__(self):
        return self.title
