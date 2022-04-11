from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import CommentForm, SubmitPostForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class PostList(generic.ListView):  # will inherit generic list view
    model = Post
    queryset = Post.objects.filter(status=1).order_by(
        # filter by category for nav bar
        "category", "-created_on"
    )  # status =1 filters by published posts / ordered by oldest first
    template_name = "index.html"  # view will render our Html file
    paginate_by = 12  # introduce page navigation after 10 posts

    # Codemy tutorial - create categories for navbar from Category Model
    def get_context_data(self, *args, **kwargs):

        cat_menu = Category.objects.all()
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


# Codemy Category tuturial- function to return post.Category
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {
        'cats': cats, 'category_posts': category_posts})


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
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        # Gets data from our form
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            comment_form.instance.email = (
                request.user.email
            )  # set username automatically from user
            comment_form.instance.name = (
                request.user.username
            )  # set email automatically from user
            comment = comment_form.save(commit=False)
            comment.post = post  # assigns comment to post
            comment.save()  # saves comment

        else:
            comment_form = (
                CommentForm()
            )  # if form not valid then leave an empty comment

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


# post like view
class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)  # get our post

        if post.likes.filter(
            id=request.user.id
        ).exists():  # if statement to toggle our like
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(
            reverse("post_detail", args=[slug])
        )  # reload page when we like/unlike post


# Submit post view
class SubmitPost(CreateView):
    model = Post
    form_class = SubmitPostForm
    template_name = "submit.html"


# Edit post View
class EditPost(UpdateView):

    model = Post
    template_name = "edit_post.html"
    fields = ["title", "content", "category", "excerpt"]


# Delete post View
class DeletePost(DeleteView):

    model = Post
    template_name = "delete_post.html"
    # return to Homepage after deleting post
    success_url = reverse_lazy("home")
