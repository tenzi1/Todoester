from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo')
    task = models.CharField(max_length=255)
    complete_by = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Todo'

    def __str__(self):
        return self.task
    
    