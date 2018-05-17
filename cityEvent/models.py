from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Event(models.Model):
		user = models.ForeignKey(User,default=None)
		title = models.CharField(max_length=100)
		description = RichTextUploadingField(blank=True,null=True)
		date_posted = models.DateTimeField(auto_now_add=True)
		location = models.CharField(max_length=100)
		organizers_name = models.CharField(max_length=100)
		banner = models.ImageField(default='media/images/')
		event_date = models.DateTimeField()
		# post_file = models.FileField(blank=True,null=True,upload_to="blog/files/%Y/m/$D/")
		def __str__(self):
			return self.title 