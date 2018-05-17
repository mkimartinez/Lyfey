from django.db import models
from django.contrib.auth.models import User

class Mem(models.Model):
	banner = models.ImageField(null=True)
	# publisher = models.CharField(max_length=100)
	date_posted = models.DateField(auto_now_add=True)
	title = models.CharField(max_length=100)
	publisher = models.ForeignKey(User,default=None)
	def __str__(self):
		return self.title

class Comment(models.Model):
	meme= models.ForeignKey(Mem,related_name='comments')
	user = models.CharField(max_length=100)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now=True)
	approved = models.BooleanField(default=False)

	def approved(self):
		self.approved=True
		self.save()

		def __str__(self):
			return self.user