# Generated by Django 3.1.2 on 2020-12-01 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mynew',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='news/', verbose_name='展报'),
        ),
    ]
