from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField
import django.db.models.deletion
class Category(models.Model):
	name = models.CharField(max_length=100)
	verbose_name_plural ='categories'
	def str(self):
		return self.name
# Create your models here.
class Question(models.Model):
	user = models.ForeignKey(User,default=None)
	content = RichTextUploadingField(blank=False,null=True)
	date_posted = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.content

class Answer(models.Model):
	answer_status = (
		('APPROVED','Approved'),
		('PENDING' ,'Pending'),
		('REJECTED','Rejected')
		)
	content = RichTextUploadingField(blank=True,null=True)
	date_answered = models.DateTimeField(auto_now_add=True)
	answered_by = models.ForeignKey(User,default=None,)
	question = models.ForeignKey(Question,default=None, null=True,related_name='answers',on_delete=django.db.models.deletion.SET_NULL)
	status = models.CharField(max_length=10, choices =answer_status,default='PENDING')
	def __str__(self):
		return self.content
