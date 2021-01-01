from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
# Create your views here.


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/post_list.html', context)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ['-post_date']


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/log-in'
    model = Post
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    login_url = '/log-in'
    model = Post
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    login_url = '/log-in'
    model = Post
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
