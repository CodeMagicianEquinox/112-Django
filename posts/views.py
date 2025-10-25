from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from django.urls import path
from .models import Post, Status

# Create your views here.
class PostListView(ListView):  # GET
    template_name = "posts/list.html"
    # model = Post
    published_status = Status.objects.get(name="published")
    queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        numbers = [1, 2, 3, 4, 5, 6]
        flag = True
        context["numbers"] = numbers
        context["flag"] = flag
        print(context)
        return context


class PostDetailedView(DetailView):  # GET
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"


class PostCreateView(CreateView):  # POST
    model = Post
    template_name = "posts/new.html"
    fields = ['title', 'subtitle', 'body', 'status']
    success_url = reverse_lazy('post_list')

def form_valid(self, form):
    form.instance.author