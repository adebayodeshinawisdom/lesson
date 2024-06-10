from django.urls import path
from . views import list_blog_posts

urlpatterns = [
    path('dashboard', list_blog_posts, name="blog_post_list" )
]
