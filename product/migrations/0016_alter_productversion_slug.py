# Generated by Django 4.1.7 on 2023-06-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_productversion_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productversion',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True, verbose_name='slug'),
        ),
    ]
