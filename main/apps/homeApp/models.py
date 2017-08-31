from __future__ import unicode_literals
from django.db import models
from ..movieApp.models import User, Movie

# Create your models here.



class Review(models.Model):
    user_id = models.ForeignKey(User, related_name='users')
    api_Movie_code = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100)
    content = models.CharField(max_length=140)
    score = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
