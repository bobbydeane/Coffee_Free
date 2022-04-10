from django.test import TestCase
from .models import Post


class TestViews(TestCase):
    # test if we can get homepage(index.html)
    def test_get_post_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # test if we can get Category page view(categories.html)
    def test_get_category_view(self):
        response = self.client.get('/category/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'categories.html')

    # test if we can submit a post(categories.html)
    def test_can_submit_post(self):
        response = self.client.post(
            '/submit_a_post', {'title': 'Test Submit Post'}
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit.html')
       
