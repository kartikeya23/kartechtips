from django.shortcuts import render

def home(request):
	return render('blog/home.html')