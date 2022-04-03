from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("like/<slug:slug>", views.PostLike.as_view(), name="post_like"),
    path("submit_a_post", views.SubmitPost.as_view(), name="submit"),
    path("<slug:slug>/edit/", views.EditPost.as_view(), name="edit_post"),
    path("<slug:slug>/delete/", views.DeletePost.as_view(), name="delete_post"),
]
