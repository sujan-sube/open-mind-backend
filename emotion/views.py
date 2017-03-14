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

    def get_queryset(self):
      queryset = Emotion.objects.filter(user=self.request.user)
      return queryset.order_by('-date').values('date', 'id', 'image', 'user')

    def create(self, request):
      serializer = self.get_serializer(data=request.data)

      if serializer.is_valid():
        # obtain analysis from microsoft emotion api
        # analysis = emotionanalysis(request.data['image'])
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


def emotionanalysis(image):
  pass