# Generated by Django 4.0.2 on 2022-03-22 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_product_code_product_horizontal_repeat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('vowen', 'VOWEN'), ('knitting', 'KNITTING')], default='vowen', max_length=10),
        ),
    ]