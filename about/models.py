from django.db import models
from ckeditor.fields import RichTextField


class TestModel(models.Model):
    text = RichTextField()
