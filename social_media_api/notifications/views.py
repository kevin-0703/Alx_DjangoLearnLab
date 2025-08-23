from django.shortcuts import render
from .models import Notification
from .serializers import NotificationSerializer, LikeNotificationSerializer, LikeNotificationDetailSerializer, UnLikeNotificationDetailSerializer
from posts.models import Like, Post, Comment
from posts.serializers import PostSerializer, CommentSerializer
from rest_framework import generics, get_object_or_404
from django.contrib.auth.permissions import IsAuthenticated, permissions
from rest_framework.response import Response, status

# Create your views here.
class LikePostView(generics.GenericAPIView):
    serializer_class = LikeNotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target=post
            )
            return Response({"message": "Post liked and notification sent."}, status=201)
        return Response({"message": "You have already liked this post."}, status=400)
        
class UnLikePostView(generics.RetrieveAPIView):
    serializer_class = UnLikeNotificationDetailSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({"message": "Post unliked."}, status=204)
        return Response({"message": "You have not liked this post."}, status=400)
        
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(recipient=user).order_by('-timestamp')
    
class CommentNotificationView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(author=user)
class PostNotificationView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)