# Generated by Django 4.2.13 on 2024-05-16 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EasyDineApp', '0009_rename_name_cardpayment_card_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardpayment',
            old_name='card_name',
            new_name='name1',
        ),
    ]
