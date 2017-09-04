import requests
"""
****************************************************
YOU MIGHT HAVE TO PIP INSTALL REQUESTS IF YOU DO NOT ALREADY HAVE IT
****************************************************

api key = 286abf6056d0a1338f772d1b7202e728
fandango api key (limit 2 requests per second) = 9vhazx25636z2jny7sqffqmd
"""
def get_discover(): #this gets the popular movies at from the TMDB api
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=286abf6056d0a1338f772d1b7202e728&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'
    json_data = requests.get(url).json()
    return json_data['results']

def get_movie(id): #this gets the popular movies at from the TMDB api
    # https://api.themoviedb.org/3/movie/{movie_id}?api_key=286abf6056d0a1338f772d1b7202e728&language=en-US

    # this gets the main info for the selected movie
    movie_url = 'https://api.themoviedb.org/3/movie/' + id + '?api_key=286abf6056d0a1338f772d1b7202e728&language=en-US'
    movie_data = requests.get(movie_url).json()

    #  this gets the infor about the cast
    cast_url = 'https://api.themoviedb.org/3/movie/' + id + '/credits?api_key=286abf6056d0a1338f772d1b7202e728'
    cast_data = requests.get(cast_url).json()

    # this gets the rotten tomatoes rating
    # title_string = movie_data['title'].split()
    # if len(title_string) == 1:
        # query = title_string[0]
    # else:
        # for word in title_string:
            # query.append(word+' + ')
    # rating_url = http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=9vhazx25636z2jny7sqffqmd&q=' + query + '&page_limit=1
    # rating_data = requests.get(rating_url).json()

    movie = {
        "movie_info": movie_data,
        "cast_info": cast_data
        # "rating_info": rating_data
    }
    return movie
