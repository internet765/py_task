# Generated by Django 4.2.3 on 2023-07-27 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_weather_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='date',
            field=models.DateTimeField(verbose_name='Дни недели'),
        ),
    ]
