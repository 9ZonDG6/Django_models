from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django_filters.views import FilterView

from . import filters
from .filters import PostFilter
from .models import Post


# Create your views here.
class PostListView(FilterView):
    template_name = 'mess_temp/mess_list.html'
    model = Post
    context_object_name = 'posts'
    filterset_class = PostFilter


class PostDetailView(DetailView):
    template_name = 'mess_temp/mess_detail.html'
    model = Post
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    template_name = 'mess_temp/mess_form.html'
    model = Post
    context_object_name = 'post'
    fields = ['post_subject', 'author', 'post_text']

    def get_success_url(self):
        return reverse_lazy('PostDetail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    template_name = 'mess_temp/mess_confirm_delete.html'
    model = Post
    context_object_name = 'post'

    def get_success_url(self):
        return reverse_lazy('Posts')


class PostCreateView(CreateView):
    template_name = 'mess_temp/mess_create.html'
    model = Post
    context_object_name = 'post'
    fields = ['post_subject', 'author', 'post_text']

    def get_success_url(self):
        return reverse_lazy('Posts')
