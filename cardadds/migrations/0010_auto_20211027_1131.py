# Generated by Django 3.2.8 on 2021-10-27 03:31

import cardadds.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardadds', '0009_auto_20211027_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backgroundimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=cardadds.models.save_image_location),
        ),
        migrations.AlterField(
            model_name='backgroundimage',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
