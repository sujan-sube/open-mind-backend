# from django.contrib.auth.models import User
# from rest_framework.decorators import list_route
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from journal.serializers import JournalSerializer
from journal.filters import JournalFilter
from journal.models import Journal

# imports for text analytics
import http.client, urllib.request, urllib.parse, urllib.error, base64, json

class JournalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = JournalFilter

    # def list(self, request):
    #   serializer = self.get_serializer(queryset, many=True)
    #   data_to_json = { "result": serializer.data }
    #   return Response(data_to_json)

    def get_queryset(self):
      queryset = Journal.objects.filter(user=self.request.user)
      return queryset.order_by('-date').values('date', 'id', 'user', 'content', 'analysis', 'analysis_comment')

    def create(self, request):
      serializer = self.get_serializer(data=request.data)

      if serializer.is_valid():
        # obtain score from micrsoft text analytics
        score = textanalysis(request.data['content'])
        comment = scoreToComment(score)
        serializer.save(user=self.request.user, analysis=score, analysis_comment=comment)
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
      data = response.read().decode('utf8')
      parsedData = json.loads(data)
      score = parsedData['documents'][0]['score']
      conn.close()
  except Exception as e:
      # print("[Errno {0}] {1}".format(e.errno, e.strerror))
      print("Error with Microsoft Cognitive Services Text Analytics API!")

  # set minimum threshold for score
  if score < 0.1:
    score = 0.1

  return score


def scoreToComment(score):
  try:  
    if score >= 0 and score < 0.2 :
      comment = "Very Unhappy"
    elif score >= 0.2 and score < 0.4 :
      comment = "Unhappy"
    elif score >= 0.4 and score < 0.6 :
      comment = "Neutral"
    elif score >= 0.6 and score < 0.8 :
      comment = "Happy" 
    elif score >= 0.8 and score <= 1.0 :
      comment = "Very Happy"
  except Exception as e:
    print("Error converting score to comment")
    comment = None

  return comment
