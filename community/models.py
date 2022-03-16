from django.db import models
from django.contrib.auth.models import User
# Import Cloudinary field for or featured image
from cloudinary.models import CloudinaryField


# Create a tupple for our status
# 0 or 1 for whether the draft is published
STATUS = ((0, "Draft"), (1, "Published"))

# Convert the Database diagram to a Django model

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200), unique=True)
    # onetomany model for User
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post")
    updated_on = 
