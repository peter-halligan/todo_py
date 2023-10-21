from django.db import models

# Create your models here.
class TodoItem(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
