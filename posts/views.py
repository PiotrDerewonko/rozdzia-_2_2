from django.shortcuts import render
from posts.models import post
# Create your views here.
def post_list(request):
    posts = post.objects.all()
