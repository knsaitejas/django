from django.shortcuts import render, redirect
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^delete/(?P<id>\d+)$', views.delete),
	url(r'^remove/(?P<id>\d+)$', views.remove),
	url(r'^add$', views.add)
]

