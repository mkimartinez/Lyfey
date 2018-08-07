#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from .models import Subscribe
 

# class SubscribeForm(forms.ModelForm):
#     email = forms.CharField(
#         title=forms.CharField(widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Title of your Meme'
#             }))
#     class Meta:
#         model = Subscribe
#         fields =['email']

class SubcribeForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))

    class Meta:
        model = Subscribe
        fields=['email']



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        label=u'Username：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'username',
            'id': 'id_username',
        })
    )
    password = forms.CharField(
        label=u'Password：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 'password',
            'id': 'id_password',
        }),
    )


# class ContactForm(forms.Form):
#     yourname = forms.CharField(max_length=100)

 
        


class RegisterForm(forms.Form):
    username = forms.CharField(
        label=u'Phone Number：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'username',
            'id': 'id_username',
        }),
    )
    name = forms.CharField(
        label=u'Name：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'name',
            'id': 'id_name',
        }),
    )
    password = forms.CharField(
        label=u'Password：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'password',
            'type':'password',
            'id': 'id_password',
        }),
    )
    re_password = forms.CharField(
        label=u'Re-enter Password：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 're_password',
            'id': 'id_re_password',
        }),
    )
    email = forms.CharField(
        label=u'Email：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'email',
            'id': 'id_email',
        }),
        required=False,
    )

    photo = forms.FileField(
        label=u'Photo：',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'name': 'photo',
            'id': 'id_photo',
        }),
        required=False,
    )



class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(
        label=u'Original Password：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'old_password',
            'id': 'id_old',
        }),
    )
    new_password = forms.CharField(
        label=u'New Password：',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'name': 'new_password',
            'id': 'id_new',
        }),
    )
    repeat_password = forms.CharField(
        label=u'Reset：',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'name': 'repeat_password',
            'id': 'id_repeat',
        }),
    )
