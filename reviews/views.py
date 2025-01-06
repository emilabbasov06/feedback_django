from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Review

# Create your views here.
class ReviewView(CreateView):
  model = Review # if u use createview, then you dont need to create your own form
  form_class = ReviewForm
  template_name = 'reviews/review.html'
  success_url = '/thankyou'
  
  # def post(self, request):
  #   form = ReviewForm(request.POST)
  #   if form.is_valid():
  #     form.save()
  #     return HttpResponseRedirect('/thankyou')
    
  #   return render(request, 'reviews/review.html', {
  #     'form': form
  #   })


class ThankYouView(TemplateView):
  template_name = 'reviews/thankyou.html'
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['message'] = 'This works!'
    return context


class ReviewsListView(ListView):
  template_name = 'reviews/review_list.html'
  model = Review
  context_object_name = 'reviews'
  
  # def get_queryset(self):
  #   base_query = super().get_queryset()
  #   data = base_query.filter(rating__gt=4)
  #   return data


class ReviewDetailView(DetailView):
  template_name = 'reviews/review_detail.html'
  model = Review
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    loaded_review = self.object
    request = self.request
    fav_id = request.session['fav_review']
    context['is_fav'] = fav_id == str(loaded_review.id)
    return context


class AddFavView(View):
  def post(self, request):
    review_id = request.POST['review_id']
    request.session['fav_review'] = review_id
    return HttpResponseRedirect(f'/reviews/{review_id}')