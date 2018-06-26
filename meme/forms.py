from django import forms
from django.utils.translation import gettext_lazy as _
from meme.models import Mem,Comment

class CreateMem(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(
		attrs={
		'class':'form-control',
		'placeholder':'Title of your Meme',
		}))
	banner = forms.ImageField(widget=forms.FileInput(
		attrs={
		'class':'form-control',
		}))
	class Meta:
		model = Mem
		fields =['title','banner']
		labels ={'title':_('Meme Title'),'banner':_('Meme Banner'),}

class MemeComment(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea(
		attrs={
		'class':'form-control',
		'placeholder':'Start typing your comment...',
		}))
	class Meta:
		model= Comment
		fields=['body']