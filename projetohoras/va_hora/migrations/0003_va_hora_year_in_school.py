# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('va_hora', '0002_auto_20170713_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='va_hora',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default=' ', max_length=2),
        ),
    ]
