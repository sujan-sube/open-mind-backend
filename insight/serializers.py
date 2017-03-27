# from django.contrib.auth.models import User
from rest_framework import serializers
from insight.models import Insight

class InsightSerializer(serializers.ModelSerializer):
    topic = serializers.SerializerMethodField()

    class Meta:
        model = Insight
        exclude = ('id', 'user')

    def get_topic(self, obj):
        return obj.get_topic_display()