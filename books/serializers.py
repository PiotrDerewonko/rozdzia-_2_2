from rest_framework import serializers

from books.models import Book, Author


class BookSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'author_id', 'cover')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'nick')
