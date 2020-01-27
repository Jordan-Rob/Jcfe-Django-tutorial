from django.shortcuts import render, get_object_or_404, redirect

from .models import Article
from .forms import ArticleForm

# Create your views here.


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
