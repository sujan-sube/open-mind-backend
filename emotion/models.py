from django.db import models
from django.utils import timezone
from django.db.models import SET_NULL, CASCADE

import json

# Create your models here.
class Emotion(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey('auth.User', null=True, default=None, on_delete=SET_NULL)
  image = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=100)
  date = models.DateTimeField(default=timezone.now)
  max_expression = models.CharField(max_length=200, null=True, default=None)

class Expression(models.Model):
  emotion = models.OneToOneField('Emotion', related_name='expressions', on_delete=CASCADE)
  anger = models.DecimalField(max_digits=13, decimal_places=12)
  contempt = models.DecimalField(max_digits=13, decimal_places=12)
  disgust = models.DecimalField(max_digits=13, decimal_places=12)
  fear = models.DecimalField(max_digits=13, decimal_places=12)
  happiness = models.DecimalField(max_digits=13, decimal_places=12)
  neutral = models.DecimalField(max_digits=13, decimal_places=12)
  sadness = models.DecimalField(max_digits=13, decimal_places=12)
  surprise = models.DecimalField(max_digits=13, decimal_places=12)


  # def __str__(self):
  #   score_dict = { 'anger': float(self.anger),
  #                  'contempt': float(self.contempt),
  #                  'disgust': float(self.disgust),
  #                  'fear': float(self.fear),
  #                  'happiness': float(self.happiness),
  #                  'neutral': float(self.neutral),
  #                  'sadness': float(self.sadness),
  #                  'surprise': float(self.surprise) 
  #                }
  #   max_expression = max(score_dict, key=lambda key: score_dict[key])
  #   return max_expression
  