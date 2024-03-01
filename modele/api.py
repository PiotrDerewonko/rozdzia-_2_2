from rest_framework import routers
from posts import api_views as posts_views
from books import api_views as book_views

router = routers.DefaultRouter()
router.register('posts', posts_views.PostViewset)
router.register('author', posts_views.AuthorViewset)
router.register('book', book_views.BookViewset)
router.register('author_book', book_views.AuthorViewset)
