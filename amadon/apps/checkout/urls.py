from django.conf.urls import url, include 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^checkout', views.checkout),
	url(r'^thank_you', views.thanks),
	url(r'^$', views.index)
]