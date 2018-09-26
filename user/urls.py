from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UserDetailView, EditorDetailView, MyLoginView, logout_view

urlpatterns = [
    path('login/', MyLoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', logout_view),
    path('password_reset/', 
            auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'),
            name='password_reset'),
    
    path('<str:slug>/', UserDetailView.as_view(), name='user_info'),
    path('editor/<int:pk>', EditorDetailView.as_view() , name='user_articles'),
    
]
