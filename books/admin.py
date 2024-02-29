from django.contrib import admin
from .models import Book, Borrow, Author


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author_id']
    list_filter = ['title', 'author_id']
    search_fields = ['title']


class BoorowAdmin(admin.ModelAdmin):
    list_display = ['book', 'user_id','borrowing_date', 'is_returned', 'return_date']
    list_filter = ['book']
    search_fields = ['book']

class AuthorAdmin(admin.ModelAdmin):
    list_filter = ['nick']
    list_display = ['nick']


admin.site.register(Book, BookAdmin)
admin.site.register(Borrow, BoorowAdmin)
admin.site.register(Author, AuthorAdmin)
