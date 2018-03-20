from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	print 'hi'
	return render(request, 'index.html')

def checkout(request):
	print 'checking out'
	prices = {
		'tshirt': 19.99,
		'cup': 4.99,
		'sweater': 29.99,
		'book': 49.99
	}
	request.session['quantity'] = request.POST['quantity']
	request.session['price'] = prices[request.POST['price']]
	print request.session['price'], request.session['quantity']
	request.session['total'] = float(request.session['quantity'])*float(request.session['price'])
	if 'rsum' not in request.session:
		request.session['rsum'] = 0
	else:
		request.session['rsum'] += float(request.session['total'])
	if 'rq' not in request.session:
		request.session['rq'] = 0
	else:
		request.session['rq'] += int(request.session['quantity'])
	return redirect('/amadon/thank_you')

def thanks(request):
	print 'thank you'
	return render(request, 'checkout.html')