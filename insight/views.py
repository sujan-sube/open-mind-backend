from rest_framework import viewsets, status
from rest_framework.response import Response
from insight.models import Insight
from insight.serializers import InsightSerializer


class InsightViewSet(viewsets.ModelViewSet):
    queryset = Insight.objects.all().order_by('-date')
    serializer_class = InsightSerializer
    http_method_names = ['get']

    def get_queryset(self):
      queryset = Insight.objects.filter(user=self.request.user)
      return queryset.order_by('-date')