# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 22:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journal',
            name='user_id',
        ),
    ]
