from django.db import models
from django.db import models

class Author(models.Model):
    nick = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField(null=True)

    def __str__(self):
        return f"Nick: {self.nick}, Życiorys: {self.bio}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        'posts.Author',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Tytuł: {self.title}, opis: {self.content}, autor: {self.author.nick}"


