from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField
class Category(models.Model):
	name = models.CharField(max_length=100)
	# slug = models.CharField(max_length=100,unique=True)

	# class Meta:
	# 	ordering = ('name',)
	# 	verbose_name ='category'
	# 	verbose_name_plural ='categories'

	def str(self):
		return self.name
# Create your models here.
class Question(models.Model):
	user = models.ForeignKey(User,default=None)
	content = RichTextUploadingField(blank=True,null=True)
	date_posted = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.content


