# Generated by Django 3.1 on 2020-08-27 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20200827_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
