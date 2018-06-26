# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-19 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_answer_answered_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz.Question'),
        ),
    ]
