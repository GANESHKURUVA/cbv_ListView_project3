from django.db import models

# Create your models here.

class Students(models.Model):
    sname=models.CharField(max_length=100)
    sid=models.IntegerField()
    smarks=models.IntegerField()
    tname=models.CharField(max_length=100)
