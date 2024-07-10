# Generated by Django 5.0.6 on 2024-06-27 03:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_product_image_image_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='myapp.product'),
        ),
        migrations.AlterField(
            model_name='variant',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='myapp.product'),
        ),
    ]
