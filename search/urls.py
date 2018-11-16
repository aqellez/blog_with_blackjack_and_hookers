from django.urls import path

from .views import SearchResultListView

urlpatterns = [
    path('', SearchResultListView.as_view(), name='search_list'),
]
