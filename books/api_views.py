from rest_framework.viewsets import ModelViewSet

from books.models import Book, Author
from books.serializers import BookSerialiazer, AuthorSerializer


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerialiazer


class AuthorViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer