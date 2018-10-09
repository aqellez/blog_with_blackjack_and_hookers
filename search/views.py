from django.shortcuts import render

from django.views.generic import ListView
from core.models import Article
from django.db.models.functions import Substr, StrIndex, Concat
from django.db.models import Value as V


class SearchResultListView(ListView):
    model = Article
    template_name = 'search/search_list.html'

    def get_queryset(self):
        try:
            word = self.request.GET['search_word']
        except:
            word = ""
        q1 = Article.objects.filter(title__icontains=word)
        q2 = Article.objects.select_related().filter(tags__word__icontains=word)
        q3 = (q1 | q2).distinct()
        return q3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            word = self.request.GET['search_word']
        except:
            word = ""
        context['search_word'] = word
        return context
