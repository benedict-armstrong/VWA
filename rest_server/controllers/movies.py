from dao import get_movies_showing, get_movie, get_all_movies, add_movie

def showing_movies():
    movies = get_movies_showing()
    if (movies is None):
        return "No movies found", 404
    else:
        return {'showing_movies': movies}

def info_movie(movie_id):
    movie = get_movie(movie_id)
    if (movie is None):
        return "Movie %s not found" % (movie_id), 404
    else:
        return movie

def all_movies():
    movies = get_all_movies()
    if (movies is None):
        return "No movies found", 404
    else:
        return {'movies': movies}

def add_movie_REST():
    if not request.json or not 'name' in request.json:
        abort(400)
    else:
        movie_id = add_movie(request.json["length"], request.json["name"], request.json["release_date"])
        return jsonify(movie_id), 201