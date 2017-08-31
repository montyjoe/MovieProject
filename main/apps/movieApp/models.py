from __future__ import unicode_literals
from ..User_app.models import User
from django.db import models
from . import services


class Watchlist(models.Model): #creates a watchlist
    api_Movie_code = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    poster_path = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # objects = WatchlistManager()

    @classmethod
    def add_movie(self, data):

        user = User.objects.get(id=data['user_id'])
        movie = data['movie']
        my_watchlist = Watchlist.objects.filter(user=user)


        Watchlist.objects.create( #<-- add the movie to the watchlist
            api_Movie_code = movie['id'],
            movie_title = movie['title'],
            poster_path = movie['poster_path'],
            user = user
        )
        print "added"
        return

    @classmethod
    def remove(self, data):
        return

#this is the Model for our movies ==================
class Movie(models.Model):
    api_Movie_code = models.CharField(max_length=100)




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


    @classmethod
    def add_review(self, data):
        movie = services.get_movie(data['id'])['movie_info']

        review = Review.objects.create(
            user_id = User.objects.get(id = data['user_id']),
            content = data['content'],
            score = data['score'],
            api_Movie_code = id,
            poster_path = movie["poster_path"],
            movie_title = movie['title'],
            backdrop_path = movie['backdrop_path']
        )
        return




























        # end
