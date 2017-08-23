from django.shortcuts import render
from . import services

# Create your views here.
def movie_page(request, id):
    movie = services.get_movie(id)
    page_info = {
        'movie': movie['movie_info'],
        'cast': movie['cast_info']
    }
    return render(request, 'movieApp/movie_page.html', page_info )

def cast_page(request, id):
    person = services.get_person(id)
    return render(request, 'movieApp/cast_page.html', {'person': person})
