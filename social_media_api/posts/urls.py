from django.urls import path
from .views import PostListView, PostDetailView, CommentListView, CommentDetailView
urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:id>/', CommentDetailView.as_view(), name='comment-detail'),
]