from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import BaseModel, Review, Product
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from webapp.forms import ReviewForm, SearchForm, UserForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView

class UserUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'users/index.html'
    form_class = UserForm
    context_object_name = 'product'
    permission_required = 'webapp.add_users'

    def get_success_url(self):
        return reverse('project-view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().author.all()