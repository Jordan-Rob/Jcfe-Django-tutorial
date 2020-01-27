from django.urls import path

from .views import article_detail_view, article_list_view

app_name = 'Blog'
urlpatterns = [
    path('article/<int:id>/', article_detail_view, name='article'),
    path('articles/', article_list_view, name='articles')
]
