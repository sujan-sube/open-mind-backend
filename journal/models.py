from django.db import models
from django.utils import timezone
from django.db.models import SET_NULL

# Create your models here.
class Journal(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey('auth.User', null=True, default=None, on_delete=SET_NULL, related_name='author')
  date = models.DateTimeField(default=timezone.now().replace(microsecond=0))
  content = models.TextField()
  analysis = models.DecimalField(max_digits=10, decimal_places=8, null=True, default=None)
  analysis_comment = models.TextField(null=True, default=None)
  