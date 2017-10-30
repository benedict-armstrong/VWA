from dao import get_screenings

def screenings(movie_id):
    screenings1 = get_screenings(movie_id)
    if (screenings1 is None or len(screenings1) == 0):
        return "No Screenings Found", 404
    else:
        return {"screenings": screenings1}