from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


def upload_location(instance,filename):
	return "%s/%s" %(instance.id,filename)
# //blog categories
class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100,unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name ='category'
		verbose_name_plural ='categories'
	# def get_absolute_url(self):
	# 	return reverse('blog:post_category',args=[self.slug])

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# return reverse('blog:post_by_category',args=[self.slug])
		return  "/blog/%s/" % self.slug


# POST models here.
class Post(models.Model):
	user = models.ForeignKey(User,default=None)
	title = models.CharField(max_length=100)
	body = RichTextUploadingField(blank=True,null=True)
	date_published = models.DateTimeField(auto_now_add=True)
	tags = models.CharField(max_length=100)
	category = models.ForeignKey(Category, null=True,on_delete=models.CASCADE)
	image = models.ImageField(upload_to=upload_location)
	post_file = models.FileField(blank=True,null=True,upload_to="blog/files/%Y/m/$D/")
	def __str__(self):
		return self.title

class BlogComment(models.Model):
	post = models.ForeignKey(Post,default=None,related_name='comments')
	commented_by = models.ForeignKey(User,default=None)
	date=models.DateTimeField(auto_now_add=True)
	comment= models.TextField()
	approved_comment = models.BooleanField(default=False)

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return self.comment



