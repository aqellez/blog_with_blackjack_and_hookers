from django.urls import path

from .views import UserDetailView, EditorDetailView

urlpatterns = [
    path('<str:slug>/', UserDetailView.as_view(), name='user_info'),
    path('editor/<int:pk>', EditorDetailView.as_view() , name='user_articles')
]
