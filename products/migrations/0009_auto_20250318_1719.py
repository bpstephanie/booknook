# Generated by Django 3.2.25 on 2025-03-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20250303_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='friendly_name',
            field=models.CharField(default='Default Friendly Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='friendly_name',
            field=models.CharField(default='Default Friendly Name', max_length=255),
        ),
    ]
