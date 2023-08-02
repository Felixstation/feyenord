# Generated by Django 4.1.7 on 2023-05-13 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_accesorie_vendor_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('vendor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_id', to='product.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('color_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color_id', to='product.color')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='product.product')),
                ('storage_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='storage_id', to='product.storage')),
            ],
        ),
    ]
