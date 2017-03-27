from django.db import models
from django.utils import timezone
from django.db.models import SET_NULL

# Create your models here.
class Insight(models.Model):
    TOPIC_CHOICES = (
        ('emotion', 'Emotion'),
        ('physical', 'Physical Activity'),
        ('sleep', 'Sleep Activity'),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', null=True, default=None, on_delete=SET_NULL)
    date = models.DateTimeField(default=timezone.now)
    info = models.CharField(max_length=200)
    detail = models.TextField()
    topic = models.CharField(max_length=25, choices=TOPIC_CHOICES)
