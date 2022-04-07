from django.test import TestCase
from .forms import CommentForm, SubmitPostForm

# Test to check that the form body is a required field.
class TestCommentForm(TestCase):
    
    def test_comment_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())


# Test to check that the Title is a required field for submitPostForm
class TestSubmitPostForm(TestCase):
    
    def test_submit_title_is_required(self):
        form = SubmitPostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys()) 
        self.assertEqual(form.errors['title'][0], 'This field is required.') # Test if error message is return if field empty

# Test if form will submit without an Author field populated (Author field is hidden)
    def test_submit_author_is_required(self):
        form = SubmitPostForm({'author': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())