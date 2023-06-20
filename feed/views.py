from typing import Any, Dict
from django import http
from django.http import HttpResponse
from django.views.generic import TemplateView, DeleteView, FormView
from .models import Post
from .forms import PostForm
from django.contrib import messages
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context

class PostDetailView(DeleteView):
    template_name = "detail.html"
    model = Post

class AddPostView(FormView):
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = '/'

    def dispatch(self, request, *args: Any, **kwargs: Any):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        new_object = Post.objects.create(
            test = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, 'Your post was added.')
        return super().form_valid(form)