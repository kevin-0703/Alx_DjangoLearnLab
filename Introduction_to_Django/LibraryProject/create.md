from bookshelf.models import Book
In [1]: book = Book.objects.create(
...: title="1984",
...: author="George Orwell",
...: publication_year=1949)

In [2]: print(Book)
<class 'bookshelf.models.Book'>
#expected output:
#the class of the book.
