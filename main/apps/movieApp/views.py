from django.shortcuts import render, redirect
from . import movie_services
from .models import Watchlist
from ..User_app.models import User
from ..movieApp.models import MovieReview, TVReview, EpisodeReview, UserReview
# from ..homeApp import services



# Create your views here.
def movie_page(request, id): # this renders the selected individual movie page
    in_list = False
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        watchlist = Watchlist.objects.filter(user__id=user.id)
        for movie in watchlist: #<-- this is to check if movie is already in watchlist
            if movie.api_Movie_code == id:
                in_list = True


    movie = movie_services.get_movie(id)
    reviews = Review.objects.filter(api_Movie_code=id)
    print reviews
    context = { #<-- info that goes to template
        'movie': movie['movie_info'],
        'cast': movie['cast_info'],
        'reviews' : reviews,
        'in_list': in_list
    }
    return render(request, 'movieApp/movie_page.html', context)

def show_page(request, id):
    show = movie_services.get_show(id)
    return render(request, 'movieApp/tv_page.html', {'show': show})

def movie_home(request):
    result = services.get_discover()
    return render(request, 'movieApp/movies_home.html', {'result' : result})

def tv_home(request):
    shows = movie_services.popular_tv()
    return render(request, 'movieApp/tv_home.html', {'shows': shows})

def actor_home(request):
    actors = movie_services.popular_actors()
    return render(request, 'movieApp/actors_home.html', {'actors': actors})






def cast_page(request, id): # this render the info page for the individual actor
    person_info = services.get_person(id)
    person = {
        'details': person_info['details'],
        'credits': person_info['credits']
    }
    return render(request, 'movieApp/cast_page.html', person )



# ===========================
#Post Routes
# ===========================

def add_to_watchlist(request, id): # the post route adds a movie to the Users watchlist
    if request.method == 'POST':
        movie = services.get_movie(id)
        data = {
            "movie": movie['movie_info'], # this is the data for the current movie being displayed
            "user_id": request.session['user'] # the logged in user id from session
        }
        Watchlist.add_movie(data) # add movie to Watchlist
        return redirect('/movie/' + id)


def delete_from_watchlist(request, id):
    delete_me = Watchlist.objects.get(id=id)
    delete_me.delete()
    return redirect("/profile")


def makeReview(request, id):
    if 'user' not in request.session:
        return redirect('/')
    if request.method == "POST":
        # print movie['poster_path']
        data = {
            "id": id,
            "content": request.POST['content'],
            "score": request.POST['score'],
        }
        mr = MovieReview.create_review(data)
        user_id = request.session['user']
        UserReview.add_review(mr, "movie", user_id)
    return redirect('/movie/' + id)
