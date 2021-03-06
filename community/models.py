from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Import Cloudinary field for or featured image
from cloudinary.models import CloudinaryField
from django.urls import reverse

# Import slugify to generate slugs from strings
from django.utils.text import slugify


# Create a tupple for our status
# 0 or 1 for whether the draft is published
STATUS = ((0, "Draft"), (1, "Published"))

# Convert the Database diagram to a Django model


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # onetomany model for User/author
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_post")
    updated_on = models.DateTimeField(auto_now=True)

    # RichTextField for Content formatting.
    content = RichTextField(blank=True, null=True)
    # Image stored on cloudinary with default placeholder
    featured_image = CloudinaryField("image", default="placeholder")
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="user_post_likes", blank=True)
    # foreign key for Category to match the Category model.
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )

    # slugify to auto save the slug from title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    # Helper class to order out posts via created on field
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    # User submit data to the Post Model
    def get_absolute_url(self):
        return reverse("home")

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):

    # Delete comments if post is deleted
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
        )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(
        User, related_name="user_comments_likes", blank=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    # count the number of likes
    def number_of_likes(self):
        return self.likes.count()
