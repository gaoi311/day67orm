# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-11 04:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20181011_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='app01.Book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='app01.Publisher'),
        ),
    ]