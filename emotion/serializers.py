# from django.contrib.auth.models import User
from rest_framework import serializers
from emotion.models import Emotion, Expression

class ExpressionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Expression
    exclude = ('id', 'emotion',)

class EmotionSerializer(serializers.ModelSerializer):
  image = serializers.ImageField(max_length=None, use_url=True)
  expressions = ExpressionSerializer(many=False, read_only=True)
  date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ", required=False)

  class Meta:
    model = Emotion
    exclude = ('id', 'user',)
