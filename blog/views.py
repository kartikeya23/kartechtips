from django.shortcuts import render
from .models import Blog, Category, ExternalURL


def home(request):
	featured = Category.objects.get(name='Trending').blog_set.all()[:2]
	categories = Category.objects.exclude(name='Trending')
	recent = Blog.objects.order_by('-posted_on')[:2]
	return render(request, 'blog/home.html', {
		'featured': featured,
		'all_ctgs': Category.objects.all(),
		'ctgs': categories,
		'recent': recent,
		'blog_name': 'KarTechTips',
		})