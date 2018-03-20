from django.shortcuts import render
import random
# Create your views here.

def index(request):
	print 'running index function'
	request.session['activity'] = ''
	request.session['score'] = 0
	return render (request,'index.html')

def process(request):
	print 'proces function'
	output = ''
	if request.POST['building'] == 'farm':
		request.session['farm'] = int(random.randrange(10,21))
		request.session['score'] += request.session['farm']
		output = 'Earned '+str(request.session['farm'])+' from farm!'
	elif request.POST['building'] == 'cave':
		request.session['cave'] = int(random.randrange(5,11))
		request.session['score'] += request.session['cave']
		output = 'Earned '+str(request.session['cave'])+' from cave!'
	elif request.POST['building'] == 'house':
		request.session['house'] = int(random.randrange(2,6))
		request.session['score'] += request.session['house']
		output = 'Earned '+str(request.session['house'])+' from house!'
	request.session['activity'] += "<p class='win'>"+output+"</p>"
	if request.POST['building'] == 'casino':
		request.session['casino'] = int(random.randrange(-50,51))
		request.session['score'] += request.session['casino']
		if request.session['casino'] < 0:
			output = 'Entered a casino and lost '+str(request.session['casino'])+'...Ouch..'
			request.session['activity'] += "<p class='loss'>"+output+'</p>'
		else:
			output = 'Entered a casino and WON '+str(request.session['casino'])+'...Woohoo!!'
			request.session['activity'] += "<p class='win'>"+output+'</p>'
	return render (request,'index.html')