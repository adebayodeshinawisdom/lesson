from django.contrib import admin
from . models import Blog_Post, Category, Comment

# Register your models here.
admin.site.register(Blog_Post)
admin.site.register(Category)
admin.site.register(Comment)
