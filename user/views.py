from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView, CreateView
from django.contrib.auth.models import User, AnonymousUser
from core.models import Article
from .forms import EditorForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.urls import reverse_lazy


class UserDetailView(DetailView):
    model = User
    slug_field = "username"
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        articles = Article.objects.filter(author=kwargs['object'].id)
        context['articles'] = articles
        return context


class EditorCreateView(CreateView):
    model = Article
    form_class = EditorForm
    template_name = 'user/editor_detail.html'

    def get_success_url(self):
        # breakpoint()
        return ("/user/" + str(self.request.user.username))


class EditorUpdateView(UpdateView):
    model = Article
    form_class = EditorForm
    template_name = 'user/editor_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EditorUpdateView, self).get_context_data(**kwargs)
        article = Article.objects.values().get(pk=self.kwargs['pk'])
        context['form'] = self.form_class(initial=article)
        return context

    def get_success_url(self):
        return ("/articles/" + str(self.kwargs['pk']))


class EditorDeleteView(DeleteView):
    model = Article

    def get_success_url(self):
        current_user = self.request.user.username
        return reverse_lazy('user_info', kwargs={'slug':current_user})


class MyLoginView(auth_views.LoginView):
    def get_redirect_url(self):
        return '/articles/'


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/articles/')
    