from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library/library_detail.html'  # Adjust path to your templates folder
    context_object_name = 'library'  # Allows {{ library.name }} in template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add related books
        return context