from django.urls import path
from django.http import HttpResponse
from .views import post_list, post_detail, authors_list, author_detail, post_add

app_name = 'posts'

urlpatterns = [
    path('posts_list/', post_list, name='lista_postow'),
    path('post/<int:id>', post_detail, name='post'),
    path('post_add/', post_add, name='post_add'),
    path('authors_list/', authors_list, name='lista_autorow'),
    path('author/<int:id>', author_detail, name='autor'),
]
