from django.urls import path
from . import views

urlpatterns = [
  path('', views.ReviewView.as_view()),
  path('thankyou', views.ThankYouView.as_view()),
  path('reviews', views.ReviewsListView.as_view()),
  path('reviews/<int:id>', views.ReviewDetailView.as_view())
]