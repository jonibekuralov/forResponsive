# Generated by Django 4.2.11 on 2024-04-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.URLField(max_length=400),
        ),
    ]