from django.urls import path
from .views import FeedView
from .views import PostViewSet, PostDetailView, CommentViewSet, CommentDetailView
urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'list'}), name='post-list'),
    path('posts/<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentViewSet.as_view({'get': 'list'}), name='comment-list'),
    path('comments/<int:id>/', CommentDetailView.as_view(), name='comment-detail'),
    path('feed/', FeedView.as_view(), name='feed'),
]