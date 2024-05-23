from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class AboutConfederation(models.Model):
    content = RichTextUploadingField()
