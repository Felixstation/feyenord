# Generated by Django 4.1.7 on 2023-07-08 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_rename_postal_code_checkout_zipcode_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='country',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='email',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='phone',
        ),
    ]
