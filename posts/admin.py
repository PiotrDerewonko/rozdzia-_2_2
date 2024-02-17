from django.contrib import admin
from posts.models import Author, Post
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['nick', 'email', 'bio']
    list_filter = ['email']
    search_fields = ['nick']

class postAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created', 'modified', 'author_id']
    list_filter = ['title']
    search_fields = ['title', 'content']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, postAdmin)