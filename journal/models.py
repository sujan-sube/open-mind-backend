from django.db import models
from django.utils import timezone
from django.db.models import SET_NULL

# Create your models here.
class Journal(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey('auth.User', null=True, default=None, on_delete=SET_NULL)
  date = models.DateTimeField(default=timezone.now)
  content = models.TextField()