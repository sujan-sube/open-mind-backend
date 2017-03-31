# from django.contrib.auth.models import User
from rest_framework import serializers
from journal.models import Journal
from datetime import datetime

class JournalSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ", required=False)

    class Meta:
        model = Journal
        exclude = ('id', 'user',)
