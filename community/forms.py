from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)   # tells what fields we want on our form


# ModelForm allows use to fromfields for our form
class SubmitPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "author",
            "category", "content",
            "excerpt", "featured_image"
            )

        # widget code taken from Codemy tutorial
        widgets = {
            # bootstrap styling  for form
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': '',
                    'id': 'owner',
                    'type': 'hidden'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
        }
