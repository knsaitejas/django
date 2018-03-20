from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def random(request):
	context = {
		'word': get_random_string(length=14)
	}
	# session['type'] = request.POST['restart']
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 0
	return render(request,'index.html',context)

def reset(request):
	request.session['count'] = 0
	return redirect('/random_word')