from django.shortcuts import render
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/main.html",
        context={'posts': posts, 'title': 'Lista postów', 'active_tab': 'post_list'},
    )

def post_detail(request, id):
    one_post = Post.objects.get(id=id)
    author = Author.objects.get(id=one_post.author_id)
    return render(
        request=request,
        template_name="posts/post_detail.html",
        context={'post': one_post, 'title': f'Szczegóły postu o id {one_post.id}', 'author': author, 'active_tab': 'post_list'},
    )

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
