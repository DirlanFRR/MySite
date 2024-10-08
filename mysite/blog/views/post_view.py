# blog/views.py

from django.views.generic import ListView, DetailView
from blog.models import Post

class PostView(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"

class PostDetail(DetailView):
    model = Post
    template_name = "post_detail.html"
