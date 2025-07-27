from django import forms
from .models import Book

# Secure form for creating or editing a Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']  # Adjust fields as per your model

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Example sanitization logic
        if "<script>" in title.lower():
            raise forms.ValidationError("Invalid characters in title")
        return title
