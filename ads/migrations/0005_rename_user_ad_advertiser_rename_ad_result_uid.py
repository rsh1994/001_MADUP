# Generated by Django 4.0.4 on 2022-04-29 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_result_click_alter_result_conversion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='user',
            new_name='advertiser',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='ad',
            new_name='uid',
        ),
    ]
