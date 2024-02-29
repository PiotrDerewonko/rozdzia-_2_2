from django.urls import path
from django.views.generic import TemplateView, ListView, DetailView
from .models import Book, Author
from .views import AuthorDetailView, BookDetailView, UserBorrowList

app_name = 'books'

urlpatterns = [
    path('book_list', ListView.as_view(model=Book, template_name='books_list.html', paginate_by=5), name='book_list'),
    path('author_list', ListView.as_view(model=Author, template_name='authors_list.html', paginate_by=5),
         name='author_list'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('book/<int:my_param>', BookDetailView.as_view(), name='book_detail'),
    path('user_borrow/<int:user_id>', UserBorrowList.as_view(), name='user_borow_list')


]
