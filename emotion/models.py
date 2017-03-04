from django.db import models
from django.utils import timezone
from django.db.models import SET_NULL, CASCADE

# Create your models here.
class Emotion(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey('auth.User', null=True, default=None, on_delete=SET_NULL)
  url = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=100)
  date = models.DateTimeField(default=timezone.now)

class Expression(models.Model):
  emotion_id = models.OneToOneField('Emotion', on_delete=CASCADE)
  anger = models.DecimalField(max_digits=13, decimal_places=12)
  contempt = models.DecimalField(max_digits=13, decimal_places=12)
  disgust = models.DecimalField(max_digits=13, decimal_places=12)
  fear = models.DecimalField(max_digits=13, decimal_places=12)
  happiness = models.DecimalField(max_digits=13, decimal_places=12)
  neutral = models.DecimalField(max_digits=13, decimal_places=12)
  sadness = models.DecimalField(max_digits=13, decimal_places=12)
  suprise = models.DecimalField(max_digits=13, decimal_places=12)