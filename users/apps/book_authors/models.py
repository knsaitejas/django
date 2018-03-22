from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
	name = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<Book objects: {} {}>".format(self.name, self.desc)

class Author(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	books = models.ManyToManyField(Book, related_name='authors')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	def __repr__(self):
		return "<Author objects: {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.books)



# this_book = Book.objects.get(id=4)
# this_publisher = Publisher.objects.get(id=2)
# this_publisher.books.add(this_book)
