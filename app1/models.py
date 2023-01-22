from operator import mod
from django.db import models

# Create your models here.
class Student(models.Model):
    rn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    addr = models.CharField(max_length=500)
    marks = models.FloatField()

    def __str__(self):
        return f"{self.rn} Name:{self.name}"
