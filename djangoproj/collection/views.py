from django.shortcuts import render, render_to_response

def home(request):
	number=6
	return render_to_response('index.html',{
		'numb':number,
		})

def about(request):
	return render_to_response('about.html')

def contact(request):
	return render_to_response('contact.html')
# Create your views here.
