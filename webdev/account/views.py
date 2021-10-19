from django.http import request
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView
from web.models import Blog
from .models import User
from .forms import ProfileForm
from .mixins import DeleteArticleMixin, FieldsMixin, FormValidMixin, UpdateAccessMixin, DraftEditMixin, DeleteArticleMixin, PreviewMixin, AuthorsMixin


class Login(LoginView):
    def get_success_url(self):
        if self.request.user.is_superuser or self.request.user.is_staff or self.request.user.is_author:
            return reverse_lazy('account:list')
        else:
            return reverse_lazy('account:profile')


class Home(AuthorsMixin, LoginRequiredMixin, TemplateView):
    template_name = 'registration/admin.html'


class ArticleList(AuthorsMixin, LoginRequiredMixin, ListView):
    template_name = 'registration/articleList.html'
    def get_queryset(self):
        if self.request.user.is_superuser:
            return(Blog.objects.all())
        else:
            return Blog.objects.filter(author=self.request.user)


class CreateArticle(AuthorsMixin, LoginRequiredMixin, FormValidMixin, FieldsMixin, CreateView):
    model = Blog
    template_name = 'registration/articleCreate.html'


class UpdateArticle(AuthorsMixin, DraftEditMixin, LoginRequiredMixin, UpdateAccessMixin, FormValidMixin, FieldsMixin, UpdateView):
    model = Blog
    template_name = 'registration/articleUpdate.html'


class DeleteArticle(AuthorsMixin, DeleteArticleMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('account:list')
    template_name = 'registration/articleDelete.html'


class PreviewArticle(PreviewMixin, DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Blog, slug=slug)
    template_name = 'blog/articleDetail.html'


class UpdateProfile(LoginRequiredMixin, UpdateView):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self):
        return User.objects.get(pk= self.request.user.pk)

    model = User
    template_name = 'registration/profileUpdate.html'
    success_url = reverse_lazy('account:profile')
    form_class = ProfileForm


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')
