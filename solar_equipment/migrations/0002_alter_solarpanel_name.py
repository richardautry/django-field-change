# Generated by Django 4.1.6 on 2023-02-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solar_equipment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarpanel',
            name='name',
            field=models.TextField(max_length=100, unique=True),
        ),
    ]
