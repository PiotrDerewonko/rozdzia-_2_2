from django import forms
from posts.models import Author
class PostForm(forms.Form):
    title = forms.CharField(max_length=50, required=True)
    content = forms.CharField(max_length=9999, required=True)
    author = forms.ModelChoiceField(queryset=Author.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        author = cleaned_data.get('author')


class AuthorForm(forms.Form):
    nick = forms.CharField(max_length=50, required=True)
    mail = forms.EmailField(required=True)
    bio = forms.CharField(max_length=9999, required=False)

    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        mail = cleaned_data.get('mail')
        bio = cleaned_data.get('bio')