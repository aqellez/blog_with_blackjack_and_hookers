from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.contrib.auth.models import User
from core.models import Article
from .forms import EditorForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout


class UserDetailView(DetailView):
    model = User
    slug_field = "username"
    template_name = 'user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user_id = self.request.user.id
        context['articles'] = Article.objects.filter(author__id=user_id)
        return context


class EditorDetailView(UpdateView):
    model = Article
    
    form_class = EditorForm
    template_name = 'user/editor_detail.html'
    # success_url = '11'

    def get_context_data(self, **kwargs):
        context = super(EditorDetailView, self).get_context_data(**kwargs)
        article = Article.objects.values().get(pk=self.kwargs['pk'])
        context['form'] = self.form_class(initial=article)
        return context

    def get_success_url(self):
        return (str(self.kwargs['pk']))

    # def post(self, request, *args, **kwargs):
    #     # obj = self.get_object()
    #     form = self.get_form()
    #     # obj.save()
    #     return self.form_valid(form)

    # def form_valid(self, form):
    #     obj = self.get_object()
    #     obj.title = form.data.get('title')
    #     obj.body = form.data.get('body') if form.data.get('body') != '' else ' '
    #     # form.data['body'] = ' '
    #     # brea  kpoint()
    #     # obj.body = form.cleaned_data['body']  if form.cleaned_data['body'] !=
    #     obj.save()
    #     return super().form_valid(form)


class MyLoginView(auth_views.LoginView):

    def get_redirect_url(self):
        return '/articles/'


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/articles/')
    