# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-08 08:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0008_remove_answer_answered_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answered_by',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
