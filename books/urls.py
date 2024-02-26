from django.urls import path
from django.views.generic import TemplateView, ListView
from .models import Book, Author

app_name = 'books'

urlpatterns = [
    path('book_list', ListView.as_view(model=Book, template_name='books_list.html'), name='book_list'),
    path('author_list', ListView.as_view(model=Author, template_name='authors_list.html'), name='author_list'),

]
