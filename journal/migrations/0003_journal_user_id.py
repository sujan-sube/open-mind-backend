# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 22:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0002_remove_journal_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='user_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]