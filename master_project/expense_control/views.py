from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render( request, 'expense_control/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'expense_control/index.html'
    context_object_name = 'posts'
    ordering = ['-fecha']

class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'expense_control/about.html')


