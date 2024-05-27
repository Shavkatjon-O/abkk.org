# Generated by Django 5.0.6 on 2024-05-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about", "0006_aboutguides_content_en_aboutguides_content_ru_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutSymbols",
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
                ("title", models.CharField(max_length=256)),
                ("title_ru", models.CharField(max_length=256, null=True)),
                ("title_uz", models.CharField(max_length=256, null=True)),
                ("title_en", models.CharField(max_length=256, null=True)),
            ],
            options={
                "verbose_name": "Symbols",
                "verbose_name_plural": "Symbols",
            },
        ),
    ]