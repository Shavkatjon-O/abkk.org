from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class AboutConfederation(models.Model):
    title = models.CharField(max_length=256)
    content = RichTextUploadingField()

    class Meta:
        verbose_name = "Confederation"
        verbose_name_plural = "Confederation"

    def __str__(self):
        return str(self.id)
