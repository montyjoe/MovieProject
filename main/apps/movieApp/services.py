import requests
"""
****************************************************
YOU MIGHT HAVE TO PIP INSTALL REQUESTS IF YOU DO NOT ALREADY HAVE IT
****************************************************

api key = 286abf6056d0a1338f772d1b7202e728
"""



def get_movie(id): #this gets the popular movies at from the TMDB api
    # https://api.themoviedb.org/3/movie/{movie_id}?api_key=286abf6056d0a1338f772d1b7202e728&language=en-US

    # this gets the main info for the selected movie
    movie_url = 'https://api.themoviedb.org/3/movie/' + id + '?api_key=286abf6056d0a1338f772d1b7202e728&language=en-US'
    movie_data = requests.get(movie_url).json()

    #  this gets the infor about the cast
    cast_url = 'https://api.themoviedb.org/3/movie/' + id + '/credits?api_key=286abf6056d0a1338f772d1b7202e728'
    cast_data = requests.get(cast_url).json()

    movie = {
        "movie_info": movie_data,
        "cast_info": cast_data
    }
    return movie


def get_person(id):
    
    person_url = 'https://api.themoviedb.org/3/person/' + id + '?api_key=286abf6056d0a1338f772d1b7202e728&language=en-US'
    person_data = requests.get(person_url).json()

    credit_url = 'https://api.themoviedb.org/3/person/' + id +'/movie_credits?api_key=286abf6056d0a1338f772d1b7202e728&language=en-US'
    credit_date = requests.get(credit_url).json()

    person = {
        "details": person_data,
        "credits": credit_date
    }

    return person
