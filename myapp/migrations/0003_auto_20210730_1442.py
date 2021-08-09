# Generated by Django 3.1.4 on 2021-07-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210730_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='tower',
            name='capacitance',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tower',
            name='capacitive_reactance',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tower',
            name='commulative_line_loading',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tower',
            name='conductor_type',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tower',
            name='inductance_of_transmission_lines',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tower',
            name='span',
            field=models.CharField(default='', max_length=200),
        ),
    ]