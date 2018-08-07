from django import forms
from django.utils.translation import gettext_lazy as _
from contacts.models import ContactForm

class ContactForm(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(
        attrs ={
        'class':'form-control',
        'placeholder':'Enter Job name...',
        }))
    message = forms.CharField(widget=forms.Textarea(
        attrs ={
        'class':'form-control',
        'placeholder':'Enter Job name...',
        }))
    Email = forms.CharField(widget=forms.TextInput(
        attrs ={
        'class':'form-control',
        'placeholder':'Enter Your Email...',
        }))
    class Meta:
        model = ContactForm
        fields =['subject','message','Email','user']