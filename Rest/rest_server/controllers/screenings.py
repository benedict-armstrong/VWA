from dao import get_screenings, room_get_seats

def screenings(movie_id):
    screenings1 = get_screenings(movie_id)
    if (screenings1 is None or len(screenings1) == 0):
        return "No Screenings Found", 404
    else:
        return {"screenings": screenings1}

def get_seats_REST(room_id, screening_id):
    seats = room_get_seats(screening_id, room_id)
    if (seats is None):
        return "No free seats", 404
    else:
        return {"seats":seats}