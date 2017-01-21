# from django.contrib.auth.models import User
from rest_framework import serializers
from journal.models import Journal

class JournalSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Journal
    fields = ('date', 'content')
