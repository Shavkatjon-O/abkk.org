# Generated by Django 5.0.6 on 2024-05-27 09:05

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0002_history_rules"),
    ]

    operations = [
        migrations.AddField(
            model_name="history",
            name="content_en",
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name="history",
            name="content_ru",
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name="history",
            name="content_uz",
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name="history",
            name="title_en",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="history",
            name="title_ru",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="history",
            name="title_uz",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="rules",
            name="content_en",
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name="rules",
            name="content_ru",
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name="rules",
            name="content_uz",
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name="rules",
            name="title_en",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="rules",
            name="title_ru",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="rules",
            name="title_uz",
            field=models.CharField(max_length=256, null=True),
        ),
    ]