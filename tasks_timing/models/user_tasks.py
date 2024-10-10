from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, editable=False)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.description} - {self.owner}"