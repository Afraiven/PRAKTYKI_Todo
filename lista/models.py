from django.db import models
from django.contrib.auth.models import User


class Projekt(models.Model):
    nazwa = models.CharField(max_length=150)
    motyw = models.CharField(max_length=7, blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nazwa


class Todo(models.Model):
    nazwa = models.CharField(max_length=150)
    opis = models.CharField(max_length=1000, blank=True)
    autor =  models.ForeignKey(User, on_delete=models.CASCADE)
    projekt = models.ForeignKey(Projekt, on_delete=models.CASCADE, blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=15)
    priorytet = models.CharField(max_length=2, default="1")

    def __str__(self):
        return self.nazwa