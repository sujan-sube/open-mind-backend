# from django.contrib.auth.models import User
from rest_framework import serializers
from emotion.models import Emotion, Expression

class ExpressionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Expression
    exclude = ('id', 'emotion',)

class EmotionSerializer(serializers.ModelSerializer):
  user = serializers.StringRelatedField(many=False)
  image = serializers.ImageField(max_length=None, use_url=True)
  expressions = ExpressionSerializer(many=False, read_only=True)

  class Meta:
    model = Emotion
    fields = ('user', 'date', 'image', 'max_expression', 'expressions')
