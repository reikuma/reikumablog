from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class Index(ListView):
    model = Post

# 個別
class Detail(DetailView):
    model = Post

from django.views.generic.edit import CreateView

class Create(CreateView):
    model = Post
    fields = ["title", "body", "category", "tags"]

from django.views.generic.edit import UpdateView

class Update(UpdateView):
    model = Post
    fields = ["title", "body", "category", "tags"]

from django.views.generic.edit import DeleteView

class Delete(DeleteView):
    model = Post
    success_url = "/"