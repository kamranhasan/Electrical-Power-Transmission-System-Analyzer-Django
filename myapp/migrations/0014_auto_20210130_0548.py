# Generated by Django 3.1.4 on 2021-01-30 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20210106_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(default='default_GE4BJy2.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='service',
            name='picture',
            field=models.ImageField(default='anc.jpeg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='team',
            name='picture',
            field=models.ImageField(default='male.png', upload_to='https://storage.googleapis.com/nafi-consulting.appspot.com/media/'),
        ),
    ]