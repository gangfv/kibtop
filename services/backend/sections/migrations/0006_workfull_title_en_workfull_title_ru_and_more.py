# Generated by Django 4.0 on 2022-12-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0005_workfull_workfullupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='workfull',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Product name'),
        ),
        migrations.AddField(
            model_name='workfull',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Product name'),
        ),
        migrations.AddField(
            model_name='workfull',
            name='title_tr',
            field=models.CharField(max_length=255, null=True, verbose_name='Product name'),
        ),
    ]
