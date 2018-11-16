from django.urls import path

from .views import (EditorCreateView, EditorDeleteView, EditorUpdateView,
                    RegisterFormView, UserDetailView, UserLoginView,
                    logout_view)

urlpatterns = [
    path('login/', UserLoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', logout_view),
    path('register/', RegisterFormView.as_view(), name="user_register"),
    path('delete/<int:pk>/', EditorDeleteView.as_view(), name='editor_delete'),
    path('<str:slug>/', UserDetailView.as_view(), name='user_info'),
    path('editor/<int:pk>/', EditorUpdateView.as_view(), name='user_articles'),
    path('editor/new/', EditorCreateView.as_view(), name='new_articles'),
]
