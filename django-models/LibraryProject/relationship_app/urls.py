# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView
from .views import login_view, logout_view, register_view, list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
       path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
     path('register/', views.register_view, name='register'),  

    path('login/', LoginView.as_view(
        template_name='relationship_app/login.html'
    ), name='login'), 

    path('logout/', LogoutView.as_view(
        template_name='relationship_app/logout.html'
    ), name='logout'),
]
