from __future__ import unicode_literals
from django.db import models

class Actor(models.Model):
	name = models.CharField(max_length=255)

class Movie(models.Model):
	name = models.CharField(max_length= 255)
	movie = models.ForeignKey(Actor)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
