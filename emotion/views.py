from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from emotion.serializers import EmotionSerializer
from emotion.models import Emotion, Expression
from emotion.filters import EmotionFilter
from django.conf import settings
# imports for emotion analytics
import requests, io, json, time
from PIL import Image, ExifTags

class EmotionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Emotion.objects.all().order_by('-date')
    serializer_class = EmotionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = EmotionFilter

    def get_queryset(self):
      queryset = Emotion.objects.filter(user=self.request.user)
      return queryset.order_by('-date')

    def create(self, request):
      serializer = self.get_serializer(data=request.data)

      if serializer.is_valid():
        # obtain analysis from microsoft emotion api
        analysis, max_expression = emotionanalysis(request.FILES['image'])
        if analysis is not None:
          emotion = serializer.save(user=self.request.user, max_expression=max_expression)

          # create expression object using scores from microsoft api
          try:
            expression = Expression.objects.create(emotion=emotion, **analysis)
            expression.save()
          except Exception as e:
            print("Error creating Expression object!")
            print(e)
        
          return Response(serializer.data, status=status.HTTP_201_CREATED)

      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


def emotionanalysis(image):

  res_json = None

  url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
  headers = {
      # Request headers
      'Content-Type': 'application/octet-stream',
      'Ocp-Apim-Subscription-Key': 'cce223c7151c4bcf889e50b16385b0bf',
  }

  try:
    pil_image = Image.open(image)

    # auto rotate for iphone pics
    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation]=='Orientation':
            break
    exif=dict(pil_image._getexif().items())

    if exif[orientation] == 3:
        pil_image=pil_image.rotate(180, expand=True)
    elif exif[orientation] == 6:
        pil_image=pil_image.rotate(270, expand=True)
    elif exif[orientation] == 8:
        pil_image=pil_image.rotate(90, expand=True)


    # send request
    output = io.BytesIO()
    pil_image.save(output, format='JPEG')
    # pil_image.save(settings.MEDIA_ROOT+'1.jpg')
    hex_data = output.getvalue()
    res = requests.post(url=url, data=hex_data, headers=headers, timeout=None)
    res_json = json.loads(res.text)[0]['scores']
  except Exception as e:
    print("Error with Microsoft Cognitive Services Emotion Analytics API!")
    print(e)

  max_expression = findmax(res_json)
  return res_json, max_expression


def findmax(in_dict):
  if in_dict is not None:
    return max(in_dict, key=lambda key: in_dict[key])
  else:
    return None