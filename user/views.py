from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView, CreateView

from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from core.models import Article
from .forms import EditorForm


class UserDetailView(DetailView):
    model = User
    slug_field = "username"
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        articles = Article.objects.filter(author=kwargs['object'].id)
        context['articles'] = articles
        return context


class EditorCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'user.can_create'
    model = Article
    form_class = EditorForm
    template_name = 'user/editor_detail.html'

    def get_success_url(self):
        return ("/user/" + str(self.request.user.username))

    def get_login_url(self):
        return ("/user/login/")


class EditorUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'user.can_edit'
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

    def get_login_url(self):
        return ("/user/login/")


class EditorDeleteView(PermissionRequiredMixin, DeleteView):
    model = Article
    permission_required = 'user.can_edit'

    def get_success_url(self):
        current_user = self.request.user.username
        return reverse_lazy('user_info', kwargs={'slug': current_user})

    def get_login_url(self):
        return ("/user/login/")


class UserLoginView(auth_views.LoginView):
    def get_redirect_url(self):
        return '/articles/'


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/user/login/"
    template_name = 'user/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/articles/')
