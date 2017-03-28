# from django.contrib.auth.models import User
from rest_framework import serializers
from insight.models import Insight

class InsightSerializer(serializers.ModelSerializer):
    topic = serializers.SerializerMethodField()
    date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")

    class Meta:
        model = Insight
        exclude = ('id', 'user')

    def get_topic(self, obj):
        return obj.get_topic_display()