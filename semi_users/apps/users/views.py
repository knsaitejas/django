from django.shortcuts import render, redirect 
from models import *
from django.contrib import messages 

# Create your views here.

def index(request):
	context = {
		'display': User.objects.all()
	}
	return render(request, 'index.html', context)

def new(request):
	return render(request, 'new.html')

def user(request, id):
	context = {
		'id': id,
		'first_name': str(User.objects.get(id=id).first_name),
		'last_name': str(User.objects.get(id=id).last_name),
		'email': str(User.objects.get(id=id).email),
		'created_at': str(User.objects.get(id=id).created_at)
	}
	return render(request, 'user.html', context)

def edit(request, id):
	context = {
		'id': id,
		'first_name': str(User.objects.get(id=id).first_name),
		'last_name': str(User.objects.get(id=id).last_name),
		'email': str(User.objects.get(id=id).email)
	}
	return render(request, 'edit.html', context)

def update(request, id):
	change = User.objects.get(id=request.POST['id'])
	print request.POST['id']
	change.first_name = request.POST['first_name']
	change.last_name = request.POST['last_name']
	change.email = request.POST['email']
	change.save()
	return redirect('/users')

def create(request):
	errors = User.objects.basic_validator(request.POST)	
	if len(errors):
		 for tag, error in errors.iteritems():
		 	messages.error(request, error, extra_tags=tag)
		 return redirect('/users/new')
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	User.objects.create(first_name=first_name, last_name=last_name, email=email)
	return redirect('/users')

def delete(request, id):
	delete = User.objects.get(id=id)
	delete.delete()
	return redirect('/users')
