from django.db import models

# Create your models here.


class StudentModel(models.Model):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()
    age = models.IntegerField()