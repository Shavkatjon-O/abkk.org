from django.db import models

from ckeditor.fields import RichTextField

# from django_ckeditor_5.fields import


class Common(models.Model):
    title = RichTextField()
