# Generated by Django 5.0.6 on 2024-05-31 21:13

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutConfederation",
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
                "verbose_name": "Конфедерация",
                "verbose_name_plural": "Конфедерация",
            },
        ),
        migrations.CreateModel(
            name="AboutDocuments",
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
                ("title", models.CharField(blank=True, max_length=256, null=True)),
                ("title_ru", models.CharField(blank=True, max_length=256, null=True)),
                ("title_uz", models.CharField(blank=True, max_length=256, null=True)),
                ("title_en", models.CharField(blank=True, max_length=256, null=True)),
                ("document", models.FileField(upload_to="documents/")),
                ("document_ru", models.FileField(null=True, upload_to="documents/")),
                ("document_uz", models.FileField(null=True, upload_to="documents/")),
                ("document_en", models.FileField(null=True, upload_to="documents/")),
            ],
            options={
                "verbose_name": "Учредительные документы",
                "verbose_name_plural": "Учредительные документы",
            },
        ),
        migrations.CreateModel(
            name="AboutGuides",
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
                "verbose_name": "Руководство",
                "verbose_name_plural": "Руководство",
            },
        ),
        migrations.CreateModel(
            name="AboutMembership",
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
                "verbose_name": "Членство в конфедерации",
                "verbose_name_plural": "Членство в конфедерации",
            },
        ),
        migrations.CreateModel(
            name="AboutRegulations",
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
                ("title", models.CharField(blank=True, max_length=256, null=True)),
                ("title_ru", models.CharField(blank=True, max_length=256, null=True)),
                ("title_uz", models.CharField(blank=True, max_length=256, null=True)),
                ("title_en", models.CharField(blank=True, max_length=256, null=True)),
                ("document", models.FileField(upload_to="documents/")),
                ("document_ru", models.FileField(null=True, upload_to="documents/")),
                ("document_uz", models.FileField(null=True, upload_to="documents/")),
                ("document_en", models.FileField(null=True, upload_to="documents/")),
            ],
            options={
                "verbose_name": "Устав",
                "verbose_name_plural": "Устав",
            },
        ),
        migrations.CreateModel(
            name="Carousel",
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
                ("image", models.ImageField(upload_to="carousel/")),
            ],
            options={
                "verbose_name": "Изображение",
                "verbose_name_plural": "Изображения",
            },
        ),
        migrations.CreateModel(
            name="CompetitionDocuments",
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
                ("title", models.CharField(blank=True, max_length=256, null=True)),
                ("title_ru", models.CharField(blank=True, max_length=256, null=True)),
                ("title_uz", models.CharField(blank=True, max_length=256, null=True)),
                ("title_en", models.CharField(blank=True, max_length=256, null=True)),
                ("document", models.FileField(upload_to="documents/")),
                ("document_ru", models.FileField(null=True, upload_to="documents/")),
                ("document_uz", models.FileField(null=True, upload_to="documents/")),
                ("document_en", models.FileField(null=True, upload_to="documents/")),
            ],
            options={
                "verbose_name": "Документы о соревнованиях",
                "verbose_name_plural": "Документы о соревнованиях",
            },
        ),
        migrations.CreateModel(
            name="CompetitionReports",
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
                ("title", models.CharField(blank=True, max_length=256, null=True)),
                ("title_ru", models.CharField(blank=True, max_length=256, null=True)),
                ("title_uz", models.CharField(blank=True, max_length=256, null=True)),
                ("title_en", models.CharField(blank=True, max_length=256, null=True)),
                ("document", models.FileField(upload_to="documents/")),
                ("document_ru", models.FileField(null=True, upload_to="documents/")),
                ("document_uz", models.FileField(null=True, upload_to="documents/")),
                ("document_en", models.FileField(null=True, upload_to="documents/")),
            ],
            options={
                "verbose_name": "Протоколы соревнований",
                "verbose_name_plural": "Протоколы соревнований",
            },
        ),
        migrations.CreateModel(
            name="CompetitonCalendars",
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
                ("title", models.CharField(blank=True, max_length=256, null=True)),
                ("title_ru", models.CharField(blank=True, max_length=256, null=True)),
                ("title_uz", models.CharField(blank=True, max_length=256, null=True)),
                ("title_en", models.CharField(blank=True, max_length=256, null=True)),
                ("document", models.FileField(upload_to="documents/")),
                ("document_ru", models.FileField(null=True, upload_to="documents/")),
                ("document_uz", models.FileField(null=True, upload_to="documents/")),
                ("document_en", models.FileField(null=True, upload_to="documents/")),
            ],
            options={
                "verbose_name": "Календарь соревнований",
                "verbose_name_plural": "Календарь соревнований",
            },
        ),
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
        migrations.CreateModel(
            name="Gallery",
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
                ("image", models.ImageField(upload_to="gallery/")),
                ("date", models.CharField(max_length=54)),
            ],
            options={
                "verbose_name": "Галерея",
                "verbose_name_plural": "Галерея",
            },
        ),
        migrations.CreateModel(
            name="KurashHistory",
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
                "verbose_name": "История белбогли кураш",
                "verbose_name_plural": "История белбогли кураш",
            },
        ),
        migrations.CreateModel(
            name="KurashProvisions",
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
                ("title", models.CharField(blank=True, max_length=256, null=True)),
                ("title_ru", models.CharField(blank=True, max_length=256, null=True)),
                ("title_uz", models.CharField(blank=True, max_length=256, null=True)),
                ("title_en", models.CharField(blank=True, max_length=256, null=True)),
                ("document", models.FileField(upload_to="documents/")),
                ("document_ru", models.FileField(null=True, upload_to="documents/")),
                ("document_uz", models.FileField(null=True, upload_to="documents/")),
                ("document_en", models.FileField(null=True, upload_to="documents/")),
            ],
            options={
                "verbose_name": "Положения",
                "verbose_name_plural": "Положения",
            },
        ),
        migrations.CreateModel(
            name="KurashRules",
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
                "verbose_name": "Правила белбогли кураш",
                "verbose_name_plural": "Правила белбогли кураш",
            },
        ),
    ]
