from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    forename = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField(max_length=70)

class Boat(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=100)

class Crewrequest(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
