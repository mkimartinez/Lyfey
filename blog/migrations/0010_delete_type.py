# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-17 08:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Type',
        ),
    ]
