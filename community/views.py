from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import CommentForm

class PostList(generic.ListView): #will inherit generic list view
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on') # status =1 filters by published posts / ordered by oldest first
    template_name = "index.html" # view will render our Html file
    paginate_by = 6 # introduce page navigation after 6 posts
    
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST) # Gets data from our form 

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email #set username automatically from user
            comment_form.instance.name = request.user.username #set email automatically from user
            comment =comment_form.save(commit=False)
            comment.post = post #assigns comment to post
            comment.save() #saves comment

        else:
            comment_form = CommentForm() #if form not valid then leave an empty comment

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )