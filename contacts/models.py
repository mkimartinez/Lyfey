#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datashape import unicode

from django.db import models
from django.contrib.auth.models import User

# class Profile(models.Model):
# 	user = models.OneToOneField(User,on_delete=models.CASCADE)
# 	id = models.BigIntegerField(primary_key=True)
# 	location = models.CharField(max_length=100,blank=True)

class ContactForm(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    Email = models.EmailField()
    user = models.ForeignKey(User,default=None)

    def __str__(self):
    	return self.subject