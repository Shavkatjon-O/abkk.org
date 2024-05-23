from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class TestModel(models.Model):
    text = CKEditor5Field()
