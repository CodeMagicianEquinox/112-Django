from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Status

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


class PostDetailedView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"


class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]
    success_url = reverse_lazy("post_list")


class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")
