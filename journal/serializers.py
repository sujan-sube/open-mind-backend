# from django.contrib.auth.models import User
from rest_framework import serializers
from journal.models import Journal

class JournalSerializer(serializers.ModelSerializer):
  user = serializers.StringRelatedField(many=False)

  class Meta:
    model = Journal
    fields = ('user', 'date', 'content', 'analysis', 'analysis_comment')
