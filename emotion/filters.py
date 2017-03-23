import django_filters
from rest_framework import filters
from emotion.models import Emotion

class EmotionFilter(filters.FilterSet):
  # set lookup_expr='contain' to filter by YYYY-MM-DD or comment date assignment for exact
  # date = django_filters.DateFilter(name='date')
  daterange = django_filters.DateFromToRangeFilter(name='date')

  class Meta:
    model = Emotion
    fields = ['date', 'daterange']