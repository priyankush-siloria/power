# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-15 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solarapp', '0005_auto_20181015_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractorprofile',
            name='aboutcompany',
            field=models.TextField(blank=True, null=True),
        ),
    ]
