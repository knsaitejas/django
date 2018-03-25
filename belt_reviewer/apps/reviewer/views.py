from django.shortcuts import render, redirect
from models import *
from django.contrib import messages 
import bcrypt

# Create your views here.

def index(request):
	return render (request, 'index.html')

def books(request):
	if 'id' in request.session:
		context = {
			'alias': User.objects.get(id=request.session['id']).alias,
			'books': Book.objects.all(),
			'reviews': Review.objects.all()
		}
		return render (request, 'books_home.html', context)
	else:
		return redirect('/')

def add(request):
	if 'id' in request.session:
		context = {
			'books': Book.objects.all()
		}
		return render(request, 'book_review.html', context)
	else:
		return redirect('/')

def new_review(request):
	book = Book.objects.filter(name=request.POST['book_title'])
	if len(book) == 1:
		book = Book.objects.get(name=request.POST['book_title'])
		book_review = request.POST['review']
		book_rating = request.POST['rating']
		user = User.objects.get(id=request.session['id'])
		Review.objects.create(user=user, book=book, rating=book_rating, comment=book_review)
	else:
		book_title = request.POST['book_title']
		if len(request.POST['author2']) > 1:
			author = request.POST['author2']
		else:
			author = request.POST['author']
		Book.objects.create(name=book_title, author=author)
		user = User.objects.get(id=request.session['id'])
		book = Book.objects.get(name=request.POST['book_title'])
		book_review = request.POST['review']
		book_rating = request.POST['rating']
		Review.objects.create(user=user, book=book, rating=book_rating, comment=book_review)
	request.session['book_id'] = Book.objects.get(name=request.POST['book_title']).id
	return redirect ('/books/'+str(request.session['book_id']))

def add_review (request):
	review = request.POST['review']
	rating = request.POST['rating']
	book = Book.objects.get(id=request.session['book_id'])
	user = User.objects.get(id=request.session['id'])
	Review.objects.create(user=user, book=book, rating=rating, comment=review)
	return redirect ('/books/'+str(request.session['book_id']))

def book_profile(request, id):
	request.session['book_id'] = id
	if 'id' in request.session:
		context = {
			'book_title': Book.objects.get(id=request.session['book_id']).name,
			'book_author': Book.objects.get(id=request.session['book_id']).author,
			'reviews': Review.objects.filter(book=Book.objects.get(id=request.session['book_id'])),
			'user': request.session['id'],
			'book': request.session['book_id']
		}
		return render(request, 'add_book_review.html', context)
	else:
		return redirect('/')

def user_profile(request, id):
	if 'id' in request.session:
		context	= {
			'user': User.objects.get(id=request.session['id']),
			'reviews': Review.objects.filter(user=User.objects.get(id=request.session['id']))
		}
		return render(request, 'user_reviews.html', context)
	else:
		return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')

def delete(request, id):
	x = Review.objects.get(id=id)
	x.delete()
	return redirect ('/books/'+str(request.session['book_id']))

def process(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		 for tag, error in errors.iteritems():
		 	messages.error(request, error, extra_tags=tag)
		 return redirect('/')
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	alias = request.POST['alias']
	email = request.POST['email']
	password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
	User.objects.create(first_name=first_name, last_name=last_name, alias=alias, email=email, password=password)
	request.session['id'] = User.objects.get(email=email).id
	return redirect('/books')

def login(request):
	errors = User.objects.login_validator(request.POST)
	if len(errors):
		 for tag, error in errors.iteritems():
		 	messages.error(request, error, extra_tags=tag)
		 return redirect('/')
	email = request.POST['email']
	request.session['id'] = User.objects.get(email=email).id
	return redirect('/books')