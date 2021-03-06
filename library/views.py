#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django import forms
from django.contrib import auth
from library.forms import SignUpForm,SubscribeForm
from django.contrib.auth import login, authenticate
from django.template import loader
from django.contrib.auth.decorators import login_required

from library.forms import LoginForm, RegisterForm, ResetPasswordForm 

def index(request):
    return render(request, 'library/home.html')



    # return render(request, 'library/book_detail.html', {'article':article})
def contact(request):
    return render(request,'library/contact.html')


def user_login(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect('/')

    state = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse(u'Your account is disabled.')
        else:
            state = 'not_exist_or_password_error'

    context = {
        'loginForm': LoginForm(),
        'state': state,
    }

    return render(request, 'library/login.html', context)

def about(request):
    return render(request,'library/about.html')



def user_register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    registerForm = RegisterForm()

    state = None
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST, request.FILES)
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            name = request.POST.get('name', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create(username=username)
                new_user.save()
                new_reader = Reader.objects.create(user=new_user, name=name, phone=int(username))
                new_reader.photo = request.FILES['photo']
                new_reader.save()
                state = 'success'

                auth.login(request, new_user)

                context = {
                    'state': state,
                    'registerForm': registerForm,
                }
                return render(request, 'library/register.html', context)

    context = {
        'state': state,
        'registerForm': registerForm,
    }

    return render(request, 'library/register.html', context)
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('library:user_login')
    else:
        form = SignUpForm()
    return render(request, 'library/signup.html', {'form': form})

@login_required
def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')

        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'

    context = {
        'state': state,
        'resetPasswordForm': ResetPasswordForm(),
    }

    return render(request, 'library/set_password.html', context)


@login_required
def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    id = request.user.id
    try:
        user = User.objects.get(user_id=id)
    except User.DoesNotExist:
        return HttpResponse('no this id reader')

    # borrowing = Borrowing.objects.filter(user=user).exclude(date_returned__isnull=False)

    context = {
        'state': request.GET.get('state', None),
        'user': user,
        # 'borrowing': borrowing,
    }
    return render(request, 'library/profile.html', context)

def article_detail(request):
    return HttpResponse("HI")


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.user
            instance.save
            return redirect('library:index')
    else:
        form = SubscribeForm()
    return render(request,'library/subscribe.html', {'form': form})
