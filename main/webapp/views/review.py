
from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import BaseModel, Review, Product
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from webapp.forms import ReviewForm, SearchForm
# from webapp.base_view import CustomFormView, CustomListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class IndexView(ListView):
    template_name = 'review/review_index.html'
    model = Review
    context_object_name = 'review'
    ordering = ('title', '-created_ad')

    def get_queryset(self):
        return Review.objects.filter(review__user_id=self.request.user.pk).order_by('-check_in')


class ReviewView(DetailView):
    template_name = 'review/review_view.html'
    model = Review
    context_object_name = 'review'


class CreateReviewView(CreateView):
    template_name = 'review/review_create.html'
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.save()
        form.save_m2m()

        return redirect('review-view', pk=review.pk)

    def get_success_url(self):
        return reverse('review-view', kwargs={'pk': self.object.pk})


class ReviewUpdateView(PermissionRequiredMixin,UpdateView):
    model = Review
    template_name = 'review/review_update.html'
    form_class = ReviewForm
    context_object_name = 'review'
    permission_required = 'webapp.change_review'


    def get_success_url(self):
        return reverse('review-view', kwargs={'pk': self.object.pk})


class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'review/review_delete.html'
    model = Review
    context_object_name = 'review'
    permission_required = 'webapp.delete_review'

    success_url = reverse_lazy('review-list')







