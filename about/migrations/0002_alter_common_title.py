# Generated by Django 5.0.6 on 2024-05-23 10:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="common",
            name="title",
            field=ckeditor.fields.RichTextField(),
        ),
    ]