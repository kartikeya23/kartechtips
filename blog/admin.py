from django.contrib import admin
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
   exclude = ['posted_on']
   prepopulated_fields = {'slug': ('title',)}
 
class CategoryAdmin(admin.ModelAdmin):
   prepopulated_fields = {'slug': ('name',)}

admin.site.register(Blog)
admin.site.register(Category)

