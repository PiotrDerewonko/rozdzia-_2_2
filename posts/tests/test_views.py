from django.test import TestCase, Client
from posts.models import Post, Author
from datetime import datetime
class PostViewsTest(TestCase):
    def setUp(self):
        Author.objects.create(nick='test1', email='mail@com.pl', bio='test bio')
        author_id = Author.objects.latest('id')
        Post.objects.create(title='test', content='test contenrt', created=datetime.now(), modified=datetime.now(),
                            author_id=author_id.id)

    def test_post_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)