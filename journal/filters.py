import django_filters
from rest_framework import filters
from journal.models import Journal

class JournalFilter(filters.FilterSet):
  date = django_filters.DateFilter(name='date', lookup_expr='contains')
  daterange = django_filters.DateFromToRangeFilter(name='date')

  class Meta:
    model = Journal
    fields = ['date', 'daterange']