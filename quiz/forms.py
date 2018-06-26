from django import forms
from django.utils.translation import gettext_lazy as _
from quiz.models import Answer,Question

class AskQuestion(forms.ModelForm):
	content= forms.CharField(widget=forms.Textarea(
		attrs={
		'class':'form-control',
		'placeholder':'Start typing your comment...',
		}))
	class Meta:
		model=Question
		fields=['content']

class AnswerQuestion(forms.ModelForm):
	content= forms.CharField(widget=forms.Textarea(
		attrs={
		'class':'form-control',
		'placeholder':'Start typing your comment...',
		}))
	class Meta:
		model= Answer
		fields=['content']