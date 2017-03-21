from rest_framework import viewsets, status
from rest_framework.response import Response
from emotion.serializers import EmotionSerializer
from emotion.models import Emotion
from emotion.models import Expression

# imports for emotion analytics
import requests, io, json
from PIL import Image

class EmotionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Emotion.objects.all().order_by('-date')
    serializer_class = EmotionSerializer

    def get_queryset(self):
      queryset = Emotion.objects.filter(user=self.request.user)
      return queryset.order_by('-date')

    def create(self, request):
      serializer = self.get_serializer(data=request.data)

      if serializer.is_valid():
        # obtain analysis from microsoft emotion api
        analysis = emotionanalysis(request.FILES['image'])
        emotion = serializer.save(user=self.request.user)
        expression = Expression.objects.create(emotion=emotion, **analysis)
        expression.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


def emotionanalysis(image):

  url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
  headers = {
      # Request headers
      'Content-Type': 'application/octet-stream',
      'Ocp-Apim-Subscription-Key': 'cce223c7151c4bcf889e50b16385b0bf',
  }

  pil_image = Image.open(image)
  output = io.BytesIO()
  pil_image.save(output, format='JPEG')
  hex_data = output.getvalue()
  res = requests.post(url=url, data=hex_data, headers=headers)
  res_json = json.loads(res.text)[0]['scores']

  return res_json

