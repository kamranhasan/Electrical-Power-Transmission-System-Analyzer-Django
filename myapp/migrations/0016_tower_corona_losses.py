# Generated by Django 3.1.4 on 2021-08-01 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20210801_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='tower',
            name='corona_losses',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]