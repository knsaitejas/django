from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^session_words$', views.index),
	url(r'^add$', views.add),
	url(r'^reset$', views.reset)
]