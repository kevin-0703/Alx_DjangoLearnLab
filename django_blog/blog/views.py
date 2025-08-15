from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView ,DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "blog/register.html"

@login_required
def edit_profile(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        user = request.user
        user.username = username
        user.email = email
        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("edit_profile")
    return render(request, "blog/edit_profile.html")
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("post_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Post created successfully.")
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/User_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        posts = Post.objects.filter(Post=Post)
        return context

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    ordering = ["-published_date"]
 
        

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name = ("blog/post_update_form.html")
    success_url = reverse_lazy("post_list")
    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully.")
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete_form.html"
    success_url = reverse_lazy("post_list")
    def delete(self, request, *args, **kwargs):
        messages.success(request, "Post deleted successfully.")
        return super().delete(request, *args, **kwargs)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
