from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Tasks(models.Model):
    task = models.TextField(max_length=255)
    description = models.TextField(max_length=510)
    completed = models.BooleanField(default=False)
    date = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.task} = {self.user.username}"
    
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = 'Tasks'
        ordering = ['-date']