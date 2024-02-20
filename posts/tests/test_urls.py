from unittest import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404
from posts.views import post_list, post_detail, post_add

class TestUrls(TestCase):
    def test_resolutions_for_post_list(self):
        resolver = resolve('/')
        self.assertEqual(resolver.func, post_list)

    def test_resolutions_for_post_detail(self):
        resolver = resolve('/post/1')
        self.assertEqual(resolver.func, post_detail)

    def test_resolutions_for_post_add(self):
        resolver = resolve('/post_add/')
        self.assertEqual(resolver.func, post_add)
