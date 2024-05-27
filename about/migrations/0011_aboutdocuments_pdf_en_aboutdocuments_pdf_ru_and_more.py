# Generated by Django 5.0.6 on 2024-05-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0010_alter_aboutdocuments_pdf_alter_aboutregulations_pdf"),
    ]

    operations = [
        migrations.AddField(
            model_name="aboutdocuments",
            name="pdf_en",
            field=models.FileField(blank=True, null=True, upload_to="documents/"),
        ),
        migrations.AddField(
            model_name="aboutdocuments",
            name="pdf_ru",
            field=models.FileField(blank=True, null=True, upload_to="documents/"),
        ),
        migrations.AddField(
            model_name="aboutdocuments",
            name="pdf_uz",
            field=models.FileField(blank=True, null=True, upload_to="documents/"),
        ),
        migrations.AddField(
            model_name="aboutregulations",
            name="pdf_en",
            field=models.FileField(blank=True, null=True, upload_to="documents/"),
        ),
        migrations.AddField(
            model_name="aboutregulations",
            name="pdf_ru",
            field=models.FileField(blank=True, null=True, upload_to="documents/"),
        ),
        migrations.AddField(
            model_name="aboutregulations",
            name="pdf_uz",
            field=models.FileField(blank=True, null=True, upload_to="documents/"),
        ),
    ]
