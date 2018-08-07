from django.db import models
from django.contrib.auth.models import User
import django.db.models.deletion

class Mem(models.Model):
	banner = models.ImageField(null=True)
	# publisher = models.CharField(max_length=100)
	date_posted = models.DateField(auto_now_add=True)
	likes = models.ManyToManyField(User,blank=True,related_name='meme_likes')
	title = models.CharField(max_length=100)
	publisher = models.ForeignKey(User,default=None,null=True, on_delete=django.db.models.deletion.SET_NULL)
	def __str__(self):
		return self.title

class Comment(models.Model):
	meme= models.ForeignKey(Mem,default=None,related_name='comments',null=True, on_delete=django.db.models.deletion.SET_NULL)
	user = models.ForeignKey(User,default=None,blank=True,null=True, on_delete=django.db.models.deletion.SET_NULL)
	# email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now=True)
	approved = models.BooleanField(default=False)

	def approved(self):
		self.approved=True
		self.save()

		def __str__(self):
			return self.user