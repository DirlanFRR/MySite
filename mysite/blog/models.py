from django.db import models
from django.contrib.auth.models import User

# STATUS choices
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

# Modelo Post
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Modelo BlogPost (antes estava no post.py)
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
