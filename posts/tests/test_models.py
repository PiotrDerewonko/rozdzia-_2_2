from unittest import TestCase
from posts.models import Post, Author
from datetime import datetime
class PostModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick='test1', email='mail@com.pl', bio='test bio')
        author_id = Author.objects.latest('id')
        Post.objects.create(title='test', content='test contenrt', created=datetime.now(), modified=datetime.now(),
                            author_id=author_id.id)

    def test_post_str(self):
        post_1 = Post.objects.latest('id')
        self.assertEqual(str(post_1), f"Tytuł: test, opis: test contenrt, autor: test1")
