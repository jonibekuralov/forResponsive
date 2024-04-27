# Generated by Django 5.0.4 on 2024-04-21 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='author',
            field=models.CharField(max_length=20),
        ),
    ]
