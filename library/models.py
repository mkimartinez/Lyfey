#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datashape import unicode
from django.db import models
from django.contrib.auth.models import User
import django.db.models.deletion


# class Profile(models.Model):
# 	user = models.OneToOneField(User,on_delete=models.CASCADE)
# 	id = models.BigIntegerField(primary_key=True)
# 	location = models.CharField(max_length=100,blank=True)

class Subscribe(models.Model):
    username = models.ForeignKey(User, default=None,null=True, on_delete=django.db.models.deletion.SET_NULL)
    email = models.CharField(max_length=100)
    date_of_subscribe = models.DateField(auto_now=True)

    def __str__(self):
        return self.email

