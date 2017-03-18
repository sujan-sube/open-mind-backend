import django_filters
from rest_framework import filters
from journal.models import Journal

class JournalFilter(filters.FilterSet):
  # set lookup_expr='contain' to filter by YYYY-MM-DD or comment date assignment for exact
  # date = django_filters.DateFilter(name='date')
  daterange = django_filters.DateFromToRangeFilter(name='date')

  class Meta:
    model = Journal
    fields = ['date', 'daterange']