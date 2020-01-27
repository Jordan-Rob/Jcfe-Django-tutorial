#from django.shortcuts import render, get_object_or_404, redirect

from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)

from .models import Article
from .forms import ArticleForm

# Create your views here.

"""
def article_detail_view(request, id):
    item = Article.objects.get(id=id)
    context = {
        "item": item
    }
    return render(request, "Blog/article_detail.html", context)


def article_list_view(request):
    items = Article.objects.all()
    context = {
        "items": items
    }
    return render(request, "Blog/article_list.html", context)
"""


class ArticlelistView(ListView):
    template_name = 'Blog/article_list.html'
    queryset = Article.objects.all()  # <blog>/<modelname>_list.html


class ArticleDetailView(DeleteView):
    template_name = 'blog/article_detail.html'
    queryset = Article.objects.all()
