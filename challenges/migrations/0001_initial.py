# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-06 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('used', models.PositiveIntegerField()),
                ('difficulty', models.CharField(choices=[(1, 'Beginner'), (2, 'Medium'), (1, 'Hard')], default=1, max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]