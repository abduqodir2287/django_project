from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Teachers(models.Model):
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=35)
    date = models.DateTimeField(auto_now=True)

