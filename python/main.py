#import connexion
from flask import Flask, jsonify, abort, make_response, request
from dao import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

######### error ########

@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)

######### Get ##########

@app.route('/movies', methods=['GET'])
def showing_movies():
    movies = get_movies_showing()
    return jsonify({'showing_movies': movies})

@app.route('/users/all', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify({'users': users})

@app.route('/rooms', methods=['GET'])
def get_rooms():
    rooms = get_all_rooms()
    return jsonify({'rooms': rooms})

@app.route('/cinemas', methods=['GET'])
def get_cinemas():
    cinemas = get_all_cinemas()
    return jsonify({'cinemas': cinemas})

@app.route('/movies/all', methods=['GET'])
def all_movies():
    movies = get_all_movies()
    return jsonify({'Movies': movies})

@app.route('/movies/name/<movie_name>', methods=['GET'])
def info_movie_by_name(movie_name):
    movie = get_movie_by_name(movie_name)
    if (movie is None):
        abort(404)
    else:
        return jsonify(movie)

@app.route('/movies/year/<release_date>', methods=['GET'])
def info_movies_by_year(release_date):
    movies = get_movies_by_year(release_date)
    if (movies is None):
        abort(404)
    else:
        return jsonify(movies)

@app.route('/movies/<movie_id>', methods=['GET'])
def info_movie(movie_id):
    movie = get_movie(movie_id)
    if (movie is None):
        abort(404)
    else:
        return jsonify(movie)

@app.route('/movies/<movie_id>/screenings', methods=['GET'])
def screenings(movie_id):
    screenings1 = get_screenings(movie_id)
    if (screenings1 is None or len(screenings1) == 0):
        abort(404)
    else:
        return jsonify(screenings)

@app.route('/screenings', methods=['GET'])
def all_screenings():
    screenings1 = get_all_screenings()
    if (screenings1 is None or len(screenings1) == 0):
        abort(404)
    else:
        return jsonify(screenings)

@app.route('/room/<room_id>/screening/<screening_id>/seats', methods=['GET'])
def get_seats_REST(room_id, screening_id):
    seats = room_get_seats(screening_id, room_id)
    if (seats is None):
        abort(404)
    else:
        return jsonify(seats)

########## Post ############

@app.route('/movie/add', methods=['POST'])
def add_movie_REST():
    if not request.json or not 'name' in request.json:
        abort(400)
    else:
        movie_id = add_movie(request.json["length"], request.json["name"], request.json["release_date"])
        return jsonify(movie_id), 201

@app.route('/booking/new', methods=['POST'])
def new_booking():
    if not request.json or not 'screening_id' in request.json or not 'customer_id' in request.json:
        abort(400)
    booking_id = create_booking(request.json['customer_id'], request.json['screening_id'])
    return jsonify(booking_id), 201

@app.route('/ticket/new', methods=['POST'])
def new_ticket():
    if not request.json or not 'booking_id' in request.json or not 'seat_id' in request.json:
        abort(400)
    ticket_id = create_ticket(request.json['booking_id'], request.json['seat_id'])
    return jsonify(ticket_id), 201

@app.route('/room/new', methods=['POST'])
def new_room():
    if not request.json or not 'cinema_id' in request.json or not 'number' in request.json:
        abort(400)
    print request.json['cinema_id']
    room_id = create_room(request.json['cinema_id'], request.json['number'])
    return jsonify(room_id), 201

########## delete ##########

@app.route('/movie/delete/<movie_id>', methods=['DELETE'])
def delete_movie_REST(movie_id):
    remove_movie(movie_id)
    return jsonify({'result': True})

@app.route('/room/delete/<room_id>', methods=['DELETE'])
def remove_room(room_id):
    delete_room(room_id)
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)