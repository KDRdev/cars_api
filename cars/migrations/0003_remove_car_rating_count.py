# Generated by Django 3.1 on 2020-08-27 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200826_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='rating_count',
        ),
    ]
