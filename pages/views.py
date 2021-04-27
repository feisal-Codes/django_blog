from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy # new

class HomePageView(ListView):
  model=Post 
  template_name = 'home.html'

# class Aboutpage (TemplateView):
#     template_name="about.html"

class PostDetailView(DetailView):
    model=Post
    template_name="post_detail.html"

class PostCreateView(CreateView):
    model=Post
    template_name="post_new.html"
    fields=['title','body', 'post_author']

class PostEditView(UpdateView):
    model=Post
    template_name="post_edit.html"
    fields=["title", "body"]
class PostDeleteView(DeleteView):
    model=Post
    template_name="delete.html"
    success_url = reverse_lazy('home')
