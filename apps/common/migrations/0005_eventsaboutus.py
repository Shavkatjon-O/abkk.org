# Generated by Django 5.0.6 on 2024-06-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0004_galleryphoto"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventsAboutUs",
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
                ("link", models.CharField(max_length=256)),
                ("link_ru", models.CharField(max_length=256, null=True)),
                ("link_uz", models.CharField(max_length=256, null=True)),
                ("link_en", models.CharField(max_length=256, null=True)),
            ],
            options={
                "verbose_name": "СМИ о нас",
                "verbose_name_plural": "СМИ о нас",
            },
        ),
    ]