from django import forms
from . import models

# class ReviewForm(forms.Form):
#   user_name = forms.CharField(
#     label='Name',
#     error_messages={
#       'required': 'Your name must not be empty',
#       'max_length': 'Please enter a shorter name!'
#     },
#     max_length=25
#   )
#   review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea, max_length=200)
#   rating = forms.IntegerField(label='Your Rating', min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
  
  class Meta:
    model = models.Review
    fields = '__all__'
    # exclude = ['owner_comment']
    labels = {
      'user_name': 'Your name',
      'review_text': 'Your feedback',
      'rating': 'Your rating'
    }
    error_messages = {
      'user_name': {
        'required': 'Your name must not be empty',
        'max_length': 'Please enter a shorter name!'
      }
    }