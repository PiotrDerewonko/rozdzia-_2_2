from django.urls import path
from django.views.generic import TemplateView, ListView
from .models import Book, Author

app_name = 'books'

urlpatterns = [
    path('list', ListView.as_view(model=Book, template_name='books_list.html'), name='book_list')

]
