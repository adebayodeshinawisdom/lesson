from django.shortcuts import render
from . models import Blog_Post

# Create your views here.
def list_blog_posts(request):
    posts= Blog_Post.objects.all()

    return render(request, 'posts/dashboard.html', {"posts": posts})
