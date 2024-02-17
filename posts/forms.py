from django import forms

class PostForm(forms.Form):
    pass


class AuthorForm(forms.Form):
    nick = forms.CharField(max_length=50, required=True)
    mail = forms.EmailField(required=True)
    bio = forms.CharField(max_length=9999, required=False)

    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        mail = cleaned_data.get('mail')
        bio = cleaned_data.get('bio')