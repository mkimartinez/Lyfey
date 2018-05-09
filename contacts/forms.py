from django import forms
from django.utils.translation import gettext_lazy as _
from contacts.models import ContactForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields =['subject','message','Email']
        exclude =['user']
        labels = {
            'subject': _('Title'),
        }
        labels = {
            'message': _('Your Message'),
        }
        labels = {
            'Email': _('Your Email'),
        }
        error_messages = {
            'subject': {
                'max_length': _("Max letters exceeded."),
            }
        }