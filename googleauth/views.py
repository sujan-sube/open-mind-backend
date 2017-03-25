from oauth2client import client, crypt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework.permissions import IsAuthenticated

class GoogleAuth(APIView):
    
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(status.HTTP_200_OK)

    def post(self, request):
        try:
            idinfo = client.verify_id_token(request.data['token'], None)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise crypt.AppIdentityError("Wrong issuer.")

            userid = idinfo['sub']
            print(userid)

        except crypt.AppIdentityError:
            print("Invalid Token!")
            return Response(status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_200_OK)