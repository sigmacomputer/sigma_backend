# Generated by Django 5.1.3 on 2024-11-18 03:53

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_site_google_maps'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='header_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='site',
            name='header_title',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
