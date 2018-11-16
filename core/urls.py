from django.urls import path
from .views import ArticleDetailView, ArticleListView


urlpatterns = [
    path('', ArticleListView.as_view(paginate_by=6), name="article"),
    path('<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
]
