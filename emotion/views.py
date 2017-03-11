from rest_framework import viewsets, status
from rest_framework.response import Response
from emotion.serializers import EmotionSerializer
from emotion.models import Emotion

# Create your views here.

class EmotionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Emotion.objects.all().order_by('-date')
    serializer_class = EmotionSerializer

    def list(self, request):
      queryset = Emotion.objects.all().order_by('-date').values('date', 'id', 'url', 'user')
      serializer = self.get_serializer(queryset, many=True)
      print(serializer.data)
      return Response(serializer.data)