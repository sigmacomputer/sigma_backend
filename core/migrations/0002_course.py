# Generated by Django 5.1.3 on 2024-11-16 05:34

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('index_order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['index_order'],
            },
        ),
    ]
