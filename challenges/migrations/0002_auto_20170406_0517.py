# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-06 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='used',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
