from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse ('<h1>Vice Verse</h1>')

def home(request):
	return render (request, 'home.html')