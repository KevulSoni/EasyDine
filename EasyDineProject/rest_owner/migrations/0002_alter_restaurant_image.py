# Generated by Django 4.2.13 on 2024-05-14 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_owner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
