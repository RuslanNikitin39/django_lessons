# Generated by Django 4.0.4 on 2022-05-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_options_alter_sensor_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
