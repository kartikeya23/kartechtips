from django.db import models
from datetime import datetime

class Category(models.Model):
	name = models.CharField(max_length=15, unique=True)
	slug = models.SlugField(max_length=15, unique=True)
	color = models.CharField(max_length=7, unique=True)

	def __str__(self):
		return self.name

	def Meta(self):
		ordering = ['name']

	def get_absolute_url(self):
		return ('blog-category', [self.slug])

class Blog(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	featured_image = models.ImageField(upload_to='blogs/images/')
	posted_on = models.DateField(auto_now_add=True, db_index=True)
	categories = models.ManyToManyField(Category)
	read_count = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title

	def Meta(self):
		ordering = ['posted_on', 'title']

	def get_absolute_url(self):
		return ('blog-post', [self.slug])

	def pub_date_short(self):
		return self.posted_on.strftime('%B %d, %Y')

	def get_tags(self):
		tags = self.categories.exclude(name='Trending')
		return tags[:2]

class ExternalURL(models.Model):
	def __init__(self):
		name = models.CharField(max_length=10, unique=True)
		link = models.URLField()
		click_count = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.name
		

