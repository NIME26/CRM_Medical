# Generated by Django 3.1.3 on 2020-11-07 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20201107_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time_appointment',
            field=models.DateField(),
        ),
    ]
