from unittest import TestCase
from posts.forms import PostForm, AuthorForm
from posts.models import Post, Author
from datetime import datetime
class PostFormTest(TestCase):
    def test_post_save(self):
        data = {"title": "test formularza", "content": "test formualrza contnent", "author": 1,
                "created": datetime.now(), "modified": datetime.now()}
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Post)

    def test_author_form_save(self):
        data = {'nick': 'test test', 'email': 'mail@com.pl', 'bio': 'test w testach'}
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        r = form.save()
        self.assertIsInstance(r, Author)