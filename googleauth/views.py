from oauth2client import client, crypt
from rest_framework import status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.contrib.auth.models import User
from django.conf import settings

class GoogleAuth(APIView):
    """
    API Endpoint to create user object from the Google idToken
    """
    permission_classes = (AllowAny,)

    def post(self, request):

        # try verifying token with google
        try:
            idinfo = client.verify_id_token(request.data['token'], None)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise crypt.AppIdentityError("Wrong issuer.")

            userid = idinfo['sub']
            email = idinfo['email']

        except crypt.AppIdentityError:
            print("Invalid Token!")
            raise exceptions.AuthenticationFailed('Invalid token')

        # create user object if not exists
        user_query = User.objects.filter(email=email)
        if not user_query:
            User.objects.create(username=userid, email=email)

        return Response(status.HTTP_200_OK)
