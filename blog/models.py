from django.db import models

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
	posted_on = models.DateField(auto_now_add=True, db_index=True)
	categories = models.ManyToManyField(Category)

	def __str__(self):
		return self.title

	def Meta(self):
		ordering = ['posted_on', 'title']

	def get_absolute_url(self):
		return ('blog-post', [self.slug])

