from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UserDetailView, EditorUpdateView, MyLoginView, \
    EditorDeleteView, EditorCreateView, logout_view

urlpatterns = [
    path('login/', MyLoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', logout_view),
    path('password_reset/', 
            auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),
            name='password_reset'),
    path('delete/<int:pk>/', EditorDeleteView.as_view(), name='editor_delete'),
    path('<str:slug>/', UserDetailView.as_view(), name='user_info'),
    path('editor/<int:pk>/', EditorUpdateView.as_view() , name='user_articles'),
    path('editor/new/', EditorCreateView.as_view(), name='new_articles'),
]
