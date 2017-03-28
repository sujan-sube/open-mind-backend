# from django.contrib.auth.models import User
from rest_framework import serializers
from journal.models import Journal

class JournalSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S%z", required=False)

    class Meta:
        model = Journal
        fields = ('date', 'content', 'analysis', 'analysis_comment')