# from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from journal.serializers import JournalSerializer
from journal.models import Journal


class JournalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Journal.objects.all().order_by('-date')
    serializer_class = JournalSerializer

    @detail_route(methods=['post'])
    def perform_create(self, serializer):
      serializer.save(user=self.request.user)

    @detail_route(methods=['get'])
    def perform_list(self, request):
      queryset = Journal.objects.all().order('-date')
      serializer = self.get_serializer(queryset, many=True)
      return Response(serializer.data)
