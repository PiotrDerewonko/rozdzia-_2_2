from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey('books.Author', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, blank=True, null=True)
    tags = models.ManyToManyField('books.Tag')
    cover = models.ImageField(upload_to='cover/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f'''Tytuł: {self.title}, Autor: {self.author}'''


class Author(models.Model):
    nick = models.CharField(max_length=50)

    def __str__(self):
        return f"Nick: {self.nick}"


class Tag(models.Model):
    word = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word


class Borrow(models.Model):
    borrowing_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    is_returned = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
