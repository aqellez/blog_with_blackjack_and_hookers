from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from django.views.generic import ListView, DetailView, FormView
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


class EditorDetailView(FormView, DetailView):
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
        # breakpoint()
        return (str(self.kwargs['pk']))
        # pass

    def post(self, request, *args, **kwargs):
        return FormView.post(self, request, *args, **kwargs)

    def form_valid(self, form):
        # import pdb; pdb.set_trace()
        obj = self.get_object()
        obj.title = form.cleaned_data['title']
        obj.body = form.cleaned_data['body']
        obj.save()
        return super().form_valid(form)


class MyLoginView(auth_views.LoginView):

    def get_redirect_url(self):
        return '/articles/'


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/articles/')
    