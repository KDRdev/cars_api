# Generated by Django 3.1 on 2020-08-26 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='rating_id',
        ),
        migrations.AddField(
            model_name='rating',
            name='car_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
            preserve_default=False,
        ),
    ]