from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView): #will inherit generic list view
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on') # status =1 filters by published posts / ordered by oldest first
    template_name = "index.html" # view will render our Html file
    paginate_by = 6 # introduce page navigation after 6 posts
