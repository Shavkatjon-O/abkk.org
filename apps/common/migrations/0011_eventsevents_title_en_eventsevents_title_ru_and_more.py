# Generated by Django 5.0.6 on 2024-06-10 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_eventsevents'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsevents',
            name='title_en',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='eventsevents',
            name='title_ru',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='eventsevents',
            name='title_uz',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
