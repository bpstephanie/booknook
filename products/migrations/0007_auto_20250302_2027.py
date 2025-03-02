# Generated by Django 3.2.25 on 2025-03-02 20:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20250228_0703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessory',
            options={'ordering': ['name'], 'verbose_name_plural': 'Accessories'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='ISBN must be either 10 or 13 digits long', regex='^\\d{10}(\\d{3})?$')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
