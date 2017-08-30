from __future__ import unicode_literals
from django.db import models
from ..User_app.models import User, Movie, Friend

# Create your models here.



class Review(models.Model):
    user_id = models.ForeignKey(User, related_name='users')
    movie_id = models.ForeignKey(Movie, related_name='movies')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
