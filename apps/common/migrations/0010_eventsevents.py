# Generated by Django 5.0.6 on 2024-06-10 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_eventsaboutus_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('image', models.ImageField(upload_to='events')),
            ],
            options={
                'verbose_name': 'Мероприятия',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
    ]