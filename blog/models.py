from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
		user = models.ForeignKey(User,default=None)
		title = models.CharField(max_length=100)
		body = models.TextField()
		date_published = models.DateTimeField(auto_now_add=True)
		tags = models.CharField(max_length=100)
		image = models.ImageField(default='media/images/')
		post_file = models.FileField(blank=True,null=True,upload_to="blog/files/%Y/m/$D/")
		def __str__(self):
			return self.title 