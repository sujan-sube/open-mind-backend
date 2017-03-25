from oauth2client import client, crypt
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

class GoogleIdAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        if not token:
            return None

        # try verifying token with google
        try:
            idinfo = client.verify_id_token(request.data['token'], None)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise crypt.AppIdentityError("Wrong issuer.")

            # userid = idinfo['sub']
            email = idinfo['email']
            print(email)

        except crypt.AppIdentityError:
            print("Invalid Token!")
            raise exceptions.AuthenticationFailed('Invalid token')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, GoogleIdAuthentication())