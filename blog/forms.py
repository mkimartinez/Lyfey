from django import forms
from . import models

class CreatePost(forms.ModelForm):
	"""create meme"""
	class Meta:
		model = models.Post
		fields =['title','body', 'tags', 'image']
		

class CreateComment(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(
		attrs ={
		'class':'form-control',
		'placeholder':'Enter your Comment...',
		}))
	class Meta:
		model = models.BlogComment
		fields =['comment']