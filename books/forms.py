from django import forms
from .models import Borrow


class BorrowForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        book = cleaned_data.get('book')
        user = cleaned_data.get('user')
    class Meta:
        model = Borrow
        fields = ['book', 'user']

