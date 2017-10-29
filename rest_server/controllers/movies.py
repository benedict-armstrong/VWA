from dao import get_movies_showing, get_movie

def showing_movies():
    movies = get_movies_showing()
    return {'showing_movies': movies}

def info_movie(movie_id):
    movie = get_movie(movie_id)
    if (movie is None):
        return "Movie %s not found" % (movie_id), 404
    else:
        return movie