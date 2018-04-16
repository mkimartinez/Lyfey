from django import forms
from meme.models import Mem

class CreateMeme(forms.ModelForm):
	"""create meme"""
	class Meta:
		model = Mem
		fields =['title','banner']
		