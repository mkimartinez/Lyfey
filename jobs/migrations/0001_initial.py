# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-07 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('date_posted', models.DateField(auto_now_add=True)),
            ],
        ),
    ]