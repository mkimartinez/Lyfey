from django import forms
from django.utils.translation import gettext_lazy as _
from meme.models import Mem,Comment

class CreateMeme(forms.ModelForm):
	"""create meme"""
	class Meta:
		model = Mem
		fields =['title','banner']
		labels = {
            'title': _('title'),
        }

class PostComment(forms.ModelForm):
	class Meta:
		model= Comment
		fields=['user','email','body']