# Generated by Django 3.1.4 on 2021-08-01 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210801_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tower',
            old_name='frequency_effect',
            new_name='skin_depth',
        ),
    ]
