from django.views.generic import (
    ListView, 
    DetailView,
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from .models import Post, Status


# ✅ List of Published Posts
class PostListView(ListView):
    template_name = "posts/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        published_status = Status.objects.get(name="published")
        return Post.objects.filter(status=published_status).order_by("-created_on")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["numbers"] = [1, 2, 3, 4, 5, 6]
        context["flag"] = True
        return context


# ✅ Detail View
class PostDetailedView(LoginRequiredMixin, DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"


# ✅ Create New Post
class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# ✅ Edit Post (author-only)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated and self.request.user == post.author:
            return True
        raise PermissionDenied


# ✅ Delete Post
class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")


# ✅ Draft Posts (Author Only)
class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/draft_list.html"
    context_object_name = "draft_posts"

    def get_queryset(self):
        draft_status = Status.objects.get(name="draft")
        return Post.objects.filter(
            status=draft_status,
            author=self.request.user
        ).order_by("-created_on")


# ✅ Archived Posts (All Users Can View)
class ArchivedPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/archived_list.html"
    context_object_name = "archived_posts"

    def get_queryset(self):
        archived_status = Status.objects.get(name="archived")
        return Post.objects.filter(status=archived_status).order_by("-created_on")
