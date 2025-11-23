from django import forms
from .models import Author, Book, AuthorDetails


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'bio']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'author', 'publisher', 'genres']


class AuthorDetailsForm(forms.ModelForm):
    class Meta:
        model = AuthorDetails
        fields = ['author', 'email', 'phone']
