# Generated by Django 4.0.2 on 2022-02-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_topbarcontent_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='topbarcontent',
            name='url',
            field=models.URLField(default='link', verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='topbarcontent',
            name='text',
            field=models.CharField(blank=True, max_length=80, verbose_name='Metin'),
        ),
    ]