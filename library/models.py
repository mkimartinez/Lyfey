#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datashape import unicode


# class Profile(models.Model):
# 	user = models.OneToOneField(User,on_delete=models.CASCADE)
# 	id = models.BigIntegerField(primary_key=True)
# 	location = models.CharField(max_length=100,blank=True)

# class ContactForm(models.Model):
#     subject = models.CharField(max_length=100)
#     message = models.TextField()
#     sender = models.EmailField()
#     user = models.ForeignKey(User,default=None)

#     def __str__(self):
#     	return self.subject