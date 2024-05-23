# Generated by Django 5.0.6 on 2024-05-23 18:52

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0002_aboutconfederation_delete_testmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="aboutconfederation",
            name="content_en",
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name="aboutconfederation",
            name="content_ru",
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name="aboutconfederation",
            name="content_uz",
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
