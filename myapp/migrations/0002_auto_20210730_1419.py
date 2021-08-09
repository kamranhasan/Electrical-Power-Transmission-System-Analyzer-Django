# Generated by Django 3.1.4 on 2021-07-30 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tower',
            name='current_carrying_capacity',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tower',
            name='frequency_effect',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tower',
            name='resistance',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tower',
            name='spacing_between_bundles_conductors',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tower',
            name='temperature_effect',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='tower',
            name='tower_height',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='tower',
            name='picture',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='tower',
            name='short_description',
            field=models.CharField(default='', max_length=2000),
        ),
    ]