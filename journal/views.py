# from django.contrib.auth.models import User
from rest_framework import viewsets, status
# from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from journal.serializers import JournalSerializer
from journal.models import Journal

# imports for text analytics
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

class JournalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Journal.objects.all().order_by('-date')
    serializer_class = JournalSerializer

    def list(self, request):
      queryset = Journal.objects.all().order_by('-date').values('date', 'id', 'user', 'content', 'analysis')
      serializer = self.get_serializer(queryset, many=True)
      json = JSONRenderer().render(serializer.data)
      return Response(json)

    def create(self, request):
      serializer = self.get_serializer(data=request.data)

      if serializer.is_valid():
        # obtain score from micrsoft text analytics
        score = textanalysis(request.data['content'])

        serializer.save(user=self.request.user, analysis=score)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# call microsoft text analytics and obtain score
def textanalysis(content):

  score = None
  headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '542c1fbc8661495a9d0d4bda84181f48',
  }

  params = urllib.parse.urlencode({ 
  })
  body = {"documents": [
          {
            "language": "en",
            "id": "string",
            "text": content
          }
        ]}
  body = json.dumps(body)

  try:
      conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
      conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, str(body), headers)
      response = conn.getresponse()
      data = json.loads(response.read())
      score = data['documents'][0]['score']
      conn.close()
  except Exception as e:
      print("[Errno {0}] {1}".format(e.errno, e.strerror))

  return score