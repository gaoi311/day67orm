# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-11 02:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20181011_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('1', '男'), ('2', '女')], max_length=32),
        ),
        migrations.AlterModelTable(
            name='person',
            table='person',
        ),
    ]
