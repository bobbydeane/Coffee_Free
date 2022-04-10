from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    # Auto generate Slug from title on admin site
    # Dict will map the field name to the fields we
    # want to generate from
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = (
        "status",
        "created_on",
        "likes",
    )  # allow admin to filter post by status, created on and likes
    summernote_fields = "content"

# Admin Summernote field for Comments


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ("name", "body", "post", "created_on", "approved")
    search_fields = ["name", "body", "email"]
    list_filter = (
        "created_on",
        "likes",
        "created_on",
    )  # allow admin to filter post by status, created on and likes
    summernote_fields = (
        "body"  # summernote Editor for the Comment body field on Admin site.
    )

    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


# Admin Summernote field for Category
@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    list_display = ("name",)
