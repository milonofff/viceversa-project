from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse ('<h1>Vice Verse</h1>')

def home(request):
	return render (request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	words = user_text.split()
	word = len(words)
	reversed_text = user_text[::-1]
	return render (request, 'reverse.html',{'usertext':user_text, 'reversedtext':reversed_text, 'word':word})

	