from django import forms
from . import models

class CreatePost(forms.ModelForm):
	"""create meme"""
	class Meta:
		model = models.Post
		fields =['title','body', 'tags', 'image']
		