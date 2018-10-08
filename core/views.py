from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView

from .models import Article, Comment


class ArticleListView(ListView):
    model = Article
    template_name = 'core/home.html'

   
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'core/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_id = kwargs['object'].id
        comments = Comment.objects.filter(article=article_id)
        context['comments'] = comments
        return context
