from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Task Categories
class TaskCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Task Status
class TaskStatus(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # A task belongs to a user
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(TaskCategory, on_delete=models.SET_NULL, null=True)  # e.g. To-Do, Work
    status = models.ForeignKey(TaskStatus, on_delete=models.SET_NULL, null=True)  # Pending, Completed, etc.
    start_time = models.TimeField()  # Time slot like 6:00 AM
    end_time = models.TimeField(null=True, blank=True)
    date = models.DateField()  # Task date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.start_time} - {self.end_time})"

    class Meta:
        ordering = ['start_time']
