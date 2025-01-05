from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review

# Create your views here.
class ReviewView(View):
  def get(self, request):
    form = ReviewForm()
    return render(request, 'reviews/review.html', {
      'form': form
    })


  def post(self, request):
    form = ReviewForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/thankyou')
    
    return render(request, 'reviews/review.html', {
      'form': form
    })


class ThankYouView(TemplateView):
  template_name = 'reviews/thankyou.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['message'] = 'This works!'
    return context


class ReviewsListView(TemplateView):
  template_name = 'reviews/review_list.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    reviews = Review.objects.all()
    context['reviews'] = reviews
    return context


class ReviewDetailView(TemplateView):
  template_name = 'reviews/review_detail.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    review = Review.objects.get(pk=kwargs['id'])
    context['review'] = review
    return context