# Generated by Django 4.0.3 on 2022-03-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_alter_feature_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='composition',
            name='icon',
            field=models.FileField(blank=True, upload_to='feature_icons'),
        ),
        migrations.AddField(
            model_name='composition',
            name='type',
            field=models.CharField(choices=[('natural', 'NATURAL'), ('not-natural', 'NOT-NATURAL')], default='vowen', max_length=20),
        ),
    ]