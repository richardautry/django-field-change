# Generated by Django 4.1.6 on 2023-02-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_equipment', '0002_alter_solarpanel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarpanel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]