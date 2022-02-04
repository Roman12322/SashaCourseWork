from django.db import models

class User(models.Model):
    Login = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=100)

class Calculations(models.Model):
    userId = models.CharField(max_length=50)
    sqn1 = models.CharField(max_length=100)
    sqn2 = models.CharField(max_length=100)
    result = models.IntegerField()
