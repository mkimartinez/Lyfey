from django import forms
from . import models

class CreateJob(forms.ModelForm):
	"""create meme"""
	class Meta:
		model = models.Job
		fields =['title', 'company_name', 'description', 'salary' ,'location']
		