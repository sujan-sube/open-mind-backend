# from django.contrib.auth.models import User
from rest_framework import serializers
from emotion.models import Emotion

class EmotionSerializer(serializers.ModelSerializer):
  user = serializers.StringRelatedField(many=False)
  image = serializers.ImageField(max_length=None, use_url=True)

  class Meta:
    model = Emotion
    fields = ('user', 'date', 'image')
