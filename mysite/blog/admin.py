from django.contrib import admin

# Register your models here.
 Post
from .models import Post

admin.site.register(Post)
=======
from blog.models.post import BlogPost

 main
