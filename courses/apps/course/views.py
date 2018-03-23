from django.shortcuts import render, redirect
from models import *
from django.contrib import messages 

# Create your views here.

def index(request):
	context = {
		'courses': Course.objects.all()	
	}
	return render(request,'index.html', context)

def add(request):
	errors = Course.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
		 	messages.error(request, error, extra_tags=tag)
		return redirect('/')
	name = request.POST['name']
	description = request.POST['description']
	Course.objects.create(name=name,description=description)
	return redirect('/')

def delete(request, id):
	if request.POST['submit'] == 'Yes! I want to delete this':
		course = Course.objects.get(id=id)
		course.delete()
	else:
		return redirect('/')	
	return redirect('/')

def remove(request, id):
	course = Course.objects.get(id=id)
	context = {
		'name': course.name,
		'description': course.description,
		'id': id
	}	
	return render(request, 'delete.html', context)
	# course = Course.objects.get(id=id)
	# course.delete()
	# return redirect('/')
