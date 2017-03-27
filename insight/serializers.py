# from django.contrib.auth.models import User
from rest_framework import serializers
from insight.models import Insight

class InsightSerializer(serializers.ModelSerializer):
  class Meta:
    model = Insight
    exclude = ('id',)
