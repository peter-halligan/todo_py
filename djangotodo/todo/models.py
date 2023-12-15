from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class ProjectItem(models.Model):
    owner = models.ForeignKey(
        User, related_name="projects", on_delete=models.CASCADE
        )
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)


class TodoItem(models.Model):
    owner = models.ForeignKey(
        User, related_name="todos", on_delete=models.CASCADE
        )
    Project = models.ForeignKey(
        ProjectItem, blank=True, null=True, on_delete=models.CASCADE
    )
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
