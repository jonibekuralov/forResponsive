# Generated by Django 4.2.11 on 2024-04-23 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_resource_calendar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='Calendar',
        ),
    ]