# Generated by Django 4.0.2 on 2022-03-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_product_is_easyclean_product_is_fr_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PhysicalTest',
        ),
        migrations.AddField(
            model_name='product',
            name='color_fastness',
            field=models.CharField(default='5-4/5', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='light_fastness',
            field=models.CharField(default=5, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='martindale',
            field=models.CharField(default=30000, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='pilling_abrasion',
            field=models.CharField(default=5, max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='seam_slippage',
            field=models.CharField(default='2,9-3,1', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='tear_strenght',
            field=models.CharField(default='195N-163N', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='tensile_strenght',
            field=models.CharField(default='1442N-1673N', max_length=50),
        ),
    ]