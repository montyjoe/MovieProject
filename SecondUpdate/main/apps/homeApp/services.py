import requests
"""
****************************************************
YOU MIGHT HAVE TO PIP INSTALL REQUESTS IF YOU DO NOT ALREADY HAVE IT
****************************************************

api key = 286abf6056d0a1338f772d1b7202e728
"""
def get_discover(): #this gets the popular movies at from the TMDB api
    url = 'https://api.themoviedb.org/3/discover/movie?api_key=286abf6056d0a1338f772d1b7202e728&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'
    json_data = requests.get(url).json()
    return json_data['results']
