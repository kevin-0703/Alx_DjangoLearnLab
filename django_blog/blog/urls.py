from django.urls import path, include
from django.views.generic import TemplateView
from .views import SignUpView
urlpatterns = [
    path("blog/", include("django.contrib.auth.urls")),
    path("blog/profile/", TemplateView.as_view(template_name="blog/profile.html"), name="profile"),
    path("logout/", TemplateView.as_view(template_name="blog/logout.html"), name="logout"),
    path("login/", TemplateView.as_view(template_name="blog/login.html"), name="login"),
    path("register/", SignUpView.as_view(), name="templates/blog/signup"),
    path("edit_profile/", TemplateView.as_view(template_name="blog/edit_profile.html"), name="edit_profile"),
]