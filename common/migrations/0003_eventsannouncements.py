# Generated by Django 5.0.6 on 2024-05-31 11:58

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0002_kurashprovisions_alter_competitiondocuments_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventsAnnouncements",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=256)),
                ("title_ru", models.CharField(max_length=256, null=True)),
                ("title_uz", models.CharField(max_length=256, null=True)),
                ("title_en", models.CharField(max_length=256, null=True)),
                ("content", ckeditor_uploader.fields.RichTextUploadingField()),
                (
                    "content_ru",
                    ckeditor_uploader.fields.RichTextUploadingField(null=True),
                ),
                (
                    "content_uz",
                    ckeditor_uploader.fields.RichTextUploadingField(null=True),
                ),
                (
                    "content_en",
                    ckeditor_uploader.fields.RichTextUploadingField(null=True),
                ),
            ],
            options={
                "verbose_name": "Анонс",
                "verbose_name_plural": "Анонс",
            },
        ),
    ]