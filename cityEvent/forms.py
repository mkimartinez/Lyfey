from django import forms
from . import models

class PostEvent(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(
		attrs ={
		'class':'form-control',
		'placeholder':'Enter Job name...',
		}))
	organizers_name = forms.CharField(widget=forms.TextInput(
		attrs ={
		'class':'form-control',
		'placeholder':'Enter The name of Organizers...',
		}))
	description = forms.CharField(widget=forms.Textarea(
		attrs ={
		'class':'form-control',
		'placeholder':'Enter Activity Description here...',
		}))
	location = forms.CharField(widget=forms.TextInput(
		attrs ={
		'class':'form-control',
		'placeholder':'Enter The venue ...',
		}))
	banner = forms.ImageField(widget=forms.FileInput(
		attrs={
		'class':'form-control',
		}))
	event_date = forms.DateTimeField(widget=forms.TimeInput(
		attrs={
		'class':'form-control',
		}))
	"""create meme"""
	class Meta:
		model = models.Event
		fields =['title', 'description' ,'location','banner','event_date']
		 