from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
import django.db.models.deletion
def upload_location(instance,filename):
	return "%s/%s" %(instance.id,filename)
# //blog categories
class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100,unique=True)
	# created_at = models.DateTimeField(auto_now_add=True,blank=True,default=None)
	# updated_at = models.DateTimeField(auto_now=True, blank=True,default= None)


	class Meta:
		ordering = ('name',)
		verbose_name ='category'
		verbose_name_plural ='categories'
	# def get_absolute_url(self):
	# 	return reverse('blog:post_category',args=[self.slug])

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:post_by_category',args=[self.slug])
		# return  "/blog/%s/" % self.slug



class Post(models.Model):
	user = models.ForeignKey(User,default=None,null=True, on_delete=django.db.models.deletion.SET_NULL)
	title = models.CharField(max_length=100)
	body = RichTextUploadingField(blank=True,null=True)
	date_published = models.DateTimeField(auto_now_add=True)
	tags = models.CharField(max_length=100)
	category = models.ForeignKey(Category, null=True, on_delete=django.db.models.deletion.SET_NULL)
	image = models.ImageField(upload_to=upload_location)
	post_file = models.FileField(blank=True,null=True,upload_to="blog/files/%Y/m/$D/")
	def __str__(self):
		return self.title

class BlogComment(models.Model):
	post = models.ForeignKey(Post,default=None,on_delete=django.db.models.deletion.SET_NULL, null=True, related_name='comments')
	commented_by = models.ForeignKey(User,default=None,on_delete=django.db.models.deletion.SET_NULL,null=True)
	date=models.DateTimeField(auto_now_add=True)
	comment= models.TextField()
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.comment



