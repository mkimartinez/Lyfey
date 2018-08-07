#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.contrib.staticfiles import views as static_views
from django.conf.urls.static import static
from django.conf import settings

import library.views as views
app_name = 'library'

urlpatterns = [
                 url(r'^$', views.index, name='index'),
                 url(r'^login/', views.user_login, name='user_login'),
                 url(r'^logout/', views.user_logout, name='user_logout'),
                 url(r'^register/', views.user_register, name='user_register'),
                 url(r'^subscribe/$', views.subscribe, name='subscribe'),
                 url(r'^set_password/', views.set_password, name='set_password'),
                 url(r'^library/static/(?P<path>.*)$', static_views.serve, name='static'),
                 url(r'^index/article_detail', views.article_detail, name='article_detail'),
                 url(r'^profile/', views.profile, name='profile'),
                 url(r'^signup/$', views.signup, name='signup'),
                 url(r'^about/', views.about, name='about'),
                 url(r'^contact/', views.contact, name='contact'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
