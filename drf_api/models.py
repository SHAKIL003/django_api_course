from django.db import models

# Create your models here.
# In this app we will use Browsable API for this Model

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
