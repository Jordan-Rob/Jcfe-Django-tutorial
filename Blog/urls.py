from django.urls import path

#from .views import article_detail_view, article_list_view, ArticlelistView
from .views import ArticlelistView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'Blog'
urlpatterns = [
    #path('article/<int:id>/', article_detail_view, name='article'),
    #path('articles/', article_list_view, name='articles')
    path('article/create/', ArticleCreateView.as_view(), name='create'),
    #path('article/<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('article/<int:id>/update/', ArticleUpdateView.as_view(), name="update"),
    path('article/<int:id>/delete/', ArticleDeleteView.as_view(), name='delete'),
    path('article/<int:id>/', ArticleDetailView.as_view(), name='article'),
    path('articles/', ArticlelistView.as_view(), name='articles')
]
