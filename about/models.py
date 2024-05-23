from django.db import models
from ckeditor.fields import RichTextField


class Common(models.Model):
    title = RichTextField()
