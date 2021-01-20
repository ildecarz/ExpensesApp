from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    nota = models.TextField(max_length=100)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nota