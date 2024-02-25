from django.shortcuts import render, redirect
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


# Create your views her
@login_required
def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="main.html",
        context={'posts': posts, 'title': 'Lista postów', 'active_tab': 'post_list'},
    )


def post_detail(request, id):
    one_post = Post.objects.get(id=id)
    author = Author.objects.get(id=one_post.author_id)
    return render(
        request=request,
        template_name="posts/post_detail.html",
        context={'post': one_post, 'title': f'Szczegóły postu o id {one_post.id}', 'author': author,
                 'active_tab': 'post_list'},
    )


def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.add_message(request,
                             messages.SUCCESS,
                             "Utworzony nowy post")

    form = PostForm()
    return render(request=request,
                  template_name="posts/post_add.html",
                  context={'form': form, 'title': 'Dodawanie nowego postu', 'active_tab': 'post_add'})


def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post', id)
    form = PostForm(instance=post)
    return render(request=request,
                  template_name="posts/post_edit.html",
                  context={'form': form, 'title': 'Edycja postu', 'active_tab': 'post_add'})


def authors_list(request):
    if request.method == 'POST':
        nick = request.POST['nick'] or None
        email = request.POST['mail'] or None
        bio = request.POST['bio'] or None
        Author.objects.get_or_create(
            nick=nick,
            bio=bio,
            email=email
        )
    authors = Author.objects.all()
    form = AuthorForm
    return render(
        request=request,
        template_name="posts/author_list.html",
        context={'authors': authors, 'title': 'Lista postów', 'active_tab': 'authors_list', 'form': form}
    )


def author_detail(request, id):
    author = Author.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/author_detail.html",
        context={'author': author, 'active_tab': 'author_detail', 'title': f'Opis autora: {author.nick}'}
    )
