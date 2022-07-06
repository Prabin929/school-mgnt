from django.db import models
import datetime
import os
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100,null=True)
    address = models.TextField(max_length=50)
    batch = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
