from django import forms
from django.utils.translation import gettext_lazy as _
from meme.models import Mem

class CreateMeme(forms.ModelForm):
	"""create meme"""
	class Meta:
		model = Mem
		fields =['title','banner']
		labels = {
            'title': _('title'),
        }
		