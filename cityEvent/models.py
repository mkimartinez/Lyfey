from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField
import django.db.models.deletion
# Create your models here.


class Event(models.Model):
	user = models.ForeignKey(User,default=None,null=True, on_delete=django.db.models.deletion.SET_NULL)
	title = models.CharField(max_length=100)
	description = RichTextUploadingField(blank=True,null=True)
	date_posted = models.DateTimeField(auto_now_add=True)
	location = models.CharField(max_length=100)
	organizers_name = models.CharField(max_length=100)
	banner = models.ImageField(default='media/images/')
	event_date = models.DateTimeField()
	county = models.CharField(max_length=100,null=True)
	email = models.CharField(max_length=100,null=True)
	phone_number = models.CharField(max_length=100,null=True)
	# post_file = models.FileField(blank=True,null=True,upload_to="blog/files/%Y/m/$D/")
	def __str__(self):
		return self.title