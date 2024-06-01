import os

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Carousel(BaseModel):
    image = models.ImageField(upload_to="carousel/")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.image.name


class Gallery(BaseModel):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="gallery/")
    date = models.CharField(max_length=54)

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"

    def __str__(self):
        return self.title


class AboutConfederation(BaseModel):
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Конфедерация"
        verbose_name_plural = "Конфедерация"


class AboutGuides(BaseModel):
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Руководство"
        verbose_name_plural = "Руководство"


class AboutDocuments(BaseModel):
    title = models.CharField(max_length=256)
    document = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = "Учредительные документы"
        verbose_name_plural = "Учредительные документы"


class AboutRegulations(BaseModel):
    title = models.CharField(max_length=256)
    document = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = "Устав"
        verbose_name_plural = "Устав"


class AboutMembership(BaseModel):
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Членство в конфедерации"
        verbose_name_plural = "Членство в конфедерации"


class CompetitonCalendars(BaseModel):
    title = models.CharField(max_length=256)
    document = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = "Календарь соревнований"
        verbose_name_plural = "Календарь соревнований"


class CompetitionReports(BaseModel):
    title = models.CharField(max_length=256)
    document = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = "Протоколы соревнований"
        verbose_name_plural = "Протоколы соревнований"


class CompetitionDocuments(BaseModel):
    title = models.CharField(max_length=256)
    document = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = "Документы о соревнованиях"
        verbose_name_plural = "Документы о соревнованиях"


class KurashHistory(BaseModel):
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "История белбогли кураш"
        verbose_name_plural = "История белбогли кураш"


class KurashRules(BaseModel):
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Правила белбогли кураш"
        verbose_name_plural = "Правила белбогли кураш"


class KurashProvisions(BaseModel):
    title = models.CharField(max_length=256)
    document = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = "Положения"
        verbose_name_plural = "Положения"


class EventsAnnouncements(BaseModel):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Анонс"
        verbose_name_plural = "Анонс"


class EventsAboutUs(BaseModel):
    title = models.CharField(max_length=256, null=True, blank=True)
    url = models.CharField(max_length=256)

    class Meta:
        verbose_name = "СМИ о нас"
        verbose_name_plural = "СМИ о нас"


class GalleryPhoto(BaseModel):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="gallery/")
    date = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Галерея Фото"
        verbose_name_plural = "Галерея Фото"

    def __str__(self):
        return self.title


class GalleryVideo(BaseModel):
    url = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Галерея Видео"
        verbose_name_plural = "Галерея Видео"
