from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=256)
    complete_by = models.DateTimeField()

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk':self.pk})