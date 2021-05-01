from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import BaseModel, Review, Product
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from webapp.forms import ReviewForm, ProductForm
# from webapp.base_view import CustomFormView, CustomListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ProductList(ListView):
    template_name = 'product/product_index.html'
    model = Product
    context_object_name = 'projects'
    ordering = ('title',)
    paginate_by = 5



class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product
    context_object_name = 'product'


class ProductCreate(PermissionRequiredMixin, CreateView):
    template_name = 'product/product_create.html'
    model = Product
    form_class = ProductForm
    permission_required = 'webapp.add_product'


    def get_success_url(self):
        return reverse('product-view', kwargs={'pk': self.object.pk})


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    model = Product
    template_name = 'product/product_update.html'
    form_class = ProductForm
    context_object_name = 'project'
    permission_required = 'webapp.change_product'


    def get_success_url(self):
        return reverse('product-view', kwargs={'pk': self.object.pk})


class ProductDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'product/product_delete.html'
    model = Product
    context_object_name = 'product'
    permission_required = 'webapp.delete_product'

    success_url = reverse_lazy('product-list')



