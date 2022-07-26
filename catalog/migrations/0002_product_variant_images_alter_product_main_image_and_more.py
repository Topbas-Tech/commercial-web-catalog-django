# Generated by Django 4.0.2 on 2022-03-04 13:40

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='variant_images',
            field=models.ImageField(blank=True, upload_to=catalog.models.Product.generate_filename),
        ),
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.ImageField(upload_to=catalog.models.Product.generate_filename),
        ),
        migrations.AlterField(
            model_name='product',
            name='style_image',
            field=models.ImageField(upload_to=catalog.models.Product.generate_filename),
        ),
        migrations.AlterField(
            model_name='product',
            name='zoom_image',
            field=models.ImageField(upload_to=catalog.models.Product.generate_filename),
        ),
    ]
