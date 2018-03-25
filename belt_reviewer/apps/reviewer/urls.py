from django.shortcuts import render, redirect
from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index), 
	# ^ load home page
	url(r'^books$', views.books),
	# ^ load main books page if succesful
	url(r'^books/add$', views.add),
	# ^ load add a new book + review page
	url(r'^books/(?P<id>\d+)$', views.book_profile),
	# ^ load book profile page
	url(r'^users/(?P<id>\d+)$', views.user_profile),
	# ^ load user profile page
	url(r'^logout$', views.logout),
	# ^ log the user out
	url(r'^add_review$', views.add_review),
	url(r'^process$', views.process),
	url(r'^login$', views.login),
	url(r'^new_review$', views.new_review),
	url(r'^delete/(?P<id>\d+)$', views.delete)
]