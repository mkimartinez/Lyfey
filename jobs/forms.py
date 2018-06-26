from django import forms
from . import models

class CreateJob(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(
		attrs ={
		'class':'form-control',
		'placeholder':'Enter Job name...',
		}))
	company_name = forms.CharField(widget=forms.TextInput(
		attrs ={
		'class':'form-control',
		'placeholder':'Enter The detailed company Name...',
		}))
	description = forms.CharField(widget=forms.Textarea(
		attrs ={
		'class':'form-control',
		'placeholder':'Enter Job Description here...',
		}))
	location = forms.CharField(widget=forms.TextInput(
		attrs ={
		'class':'form-control',
		'placeholder':'Enter The location of the company...',
		}))
	salary = forms.IntegerField(widget=forms.NumberInput(
		attrs={
		'class':'form-control',
		'placeholder':'Enter the salary in Kenya Shiilings',
		}))
	"""create meme"""
	class Meta:
		model = models.Job
		fields =['title', 'company_name', 'description', 'salary' ,'location']
		 