# Generated by Django 3.1.2 on 2020-11-27 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0002_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2020-11-27', max_length=20, verbose_name='出生日期'),
        ),
    ]