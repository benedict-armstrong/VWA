from dao import get_movies_showing

def showing_movies():
    movies = get_movies_showing()
    return {'showing_movies': movies}