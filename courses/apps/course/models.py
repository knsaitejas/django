from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
	def basic_validator(self, postData):
		errors = {}
		if len(postData['name']) < 6:
			errors['name'] = 'Name needs to be greater than 5 characters'
		if len(postData['description']) < 16:
			errors['description'] = 'Description needs to be greater than 15 characters'
		if Course.objects.filter(name=postData['name']) != []:
			errors['nime'] = 'Course already in database'
		return errors 

class Course(models.Model):
	name = models.CharField(max_length=245)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	def __repr__(self):
		return '<Course object: {} {} {}>'.format(self.name, self.description, self.created_at)
	objects = CourseManager()