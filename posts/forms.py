from django import forms
from posts.models import Author, Post

class PostForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        author = cleaned_data.get('author')

    class Meta:
        model = Post
        fields = ['title', 'content', 'author']


class AuthorForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        mail = cleaned_data.get('mail')
        bio = cleaned_data.get('bio')
    class Meta:
        model = Author
        fields = ['nick', 'email', 'bio']