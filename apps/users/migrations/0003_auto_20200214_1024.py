# Generated by Django 3.0.3 on 2020-02-14 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200214_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anonymous',
            old_name='address',
            new_name='city',
        ),
    ]