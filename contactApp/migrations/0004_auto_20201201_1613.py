# Generated by Django 3.1.2 on 2020-12-01 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0003_auto_20201127_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2020-12-01', max_length=20, verbose_name='出生日期'),
        ),
    ]