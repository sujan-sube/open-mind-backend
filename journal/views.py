# from django.contrib.auth.models import User
from rest_framework import viewsets, status
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

    def list(self, request):
      queryset = Journal.objects.all().order_by('-date').values('date', 'id', 'user', 'content')
      serializer = self.get_serializer(queryset, many=True)
      return Response(serializer.data)

    def create(self, request):
      serializer = self.get_serializer(data=request.data)

      if serializer.is_valid():
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)