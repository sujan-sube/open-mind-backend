# from django.contrib.auth.models import User
from rest_framework import viewsets
from journal.serializers import JournalSerializer
from journal.models import Journal


class JournalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Journal.objects.all().order_by('-date')
    serializer_class = JournalSerializer
