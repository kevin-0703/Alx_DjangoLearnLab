from django.urls import path
from django.views.generic import TemplateView
from .views import SignUpView, PostDetailView, PostListView, PostUpdateView, PostDeleteView, edit_profile

urlpatterns = [
    path("register/", SignUpView.as_view(), name="register"),
    path("profile/", TemplateView.as_view(template_name="blog/profile.html"), name="profile"),
    path("edit_profile/", edit_profile, name="edit_profile"),
    path("posts/", PostListView.as_view(), name="post_list"),
    path("post/new/", PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
]
