from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    id=models.URLField(primary_key=True, editable=False, default=uuid.uuid4)
    title=models.CharField(max_length=255)


    def __str__(self):
        return self.title


class Blog_Post(models.Model):
    id=models.URLField(primary_key=True, editable=False, default=uuid.uuid4)
    title=models.CharField(max_length=255)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    post_images=models.ImageField(upload_to='post_images', default="post.jpg")
    category=models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

    


    

class Comment(models.Model):
    id=models.URLField(primary_key=True, editable=False, default=uuid.uuid4)
    comment=models.CharField(max_length=255)
    post=models.ForeignKey(Blog_Post, on_delete=models.CASCADE)



    def __str__(self):
        return self.comment


