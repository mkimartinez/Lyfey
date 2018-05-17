from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# //blog categories
class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.CharField(max_length=100,unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name ='category'
		verbose_name_plural ='categories'

	def __str__(self):
		return self.name
# POST models here.
class Post(models.Model):
		user = models.ForeignKey(User,default=None)
		title = models.CharField(max_length=100)
		body = RichTextUploadingField(blank=True,null=True)
		date_published = models.DateTimeField(auto_now_add=True)
		tags = models.CharField(max_length=100)
		category = models.ForeignKey(Category, null=True,on_delete=models.CASCADE)
		image = models.ImageField(default='media/images/')
		post_file = models.FileField(blank=True,null=True,upload_to="blog/files/%Y/m/$D/")
		def __str__(self):
			return self.title 


