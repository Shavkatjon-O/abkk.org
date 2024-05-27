# Generated by Django 5.0.6 on 2024-05-27 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0008_aboutdocuments_aboutregulations"),
    ]

    operations = [
        migrations.AddField(
            model_name="aboutdocuments",
            name="title_en",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="aboutdocuments",
            name="title_ru",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="aboutdocuments",
            name="title_uz",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="aboutregulations",
            name="title_en",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="aboutregulations",
            name="title_ru",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="aboutregulations",
            name="title_uz",
            field=models.CharField(max_length=256, null=True),
        ),
    ]