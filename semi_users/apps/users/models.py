from __future__ import unicode_literals

from django.db import models

import md5

import re

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# app.secret_key = "ThisIsSecret!"

class UserManager(models.Manager):
	def basic_validator(self, postData):
		errors={}
		if len(postData['first_name']) < 2:
			errors['first_name'] = 'First name should be greater than 1 character'
		if len(postData['last_name']) < 2:
			errors['last_name'] = 'Last name should be greater than 1 character'
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = 'Email invalid'
		if not User.objects.filter(email=postData['email']) == []:
			errors['iemail'] = 'You already have an account'
		return errors


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	def __repr__(self):
		return "<User object: {} {} {} {}".format(self.first_name, self.last_name, self.email, self.created_at)
	objects = UserManager()