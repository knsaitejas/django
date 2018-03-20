from django.shortcuts import render, redirect 

def index(request):
	if 'toAdd' not in request.session:
		request.session['toAdd']  = ''
	return render (request,'index.html')

def add(request):
	color = request.POST['color']
	word = request.POST['word']

	if 'size' in request.POST:
		request.session['toAdd'] += "<p class='"+color+" "+request.POST['size']+"'>"+word+"</p>"
	else: 
		request.session['toAdd'] += "<p class='"+color+"'>"+word+"</p>"
	return redirect('/session_words')

def reset(request):
	request.session['toAdd']  = ''
	return redirect('/session_words')