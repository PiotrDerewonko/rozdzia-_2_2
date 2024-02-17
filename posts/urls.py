from django.urls import path
from django.http import HttpResponse
from .views import post_list, post_detail, authors_list, author_detail

app_name = 'posts'

urlpatterns = [
    path('posts_list/', post_list, name='lista_postow'),
    path('post/<int:id>', post_detail, name='post'),
    path('authors_list/', authors_list, name='lista_autorow'),
    path('author/<int:id>', author_detail, name='autor'),
]
