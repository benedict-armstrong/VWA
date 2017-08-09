import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

def get_db_connection():
    return psycopg2.connect("host=localhost dbname=cinema_reservation_db user=postgres password=tomturbo")

@contextmanager
def get_db_cursor():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()

"""
def connect_test():
    with get_db_cursor() as cursor:
        cursor.execute("select * from movie;")
        movie = cursor.fetchall()
        print movie

connect_test()
"""


def add_movie(length_in_minutes, name, release_date):
    with get_db_cursor() as cursor:
        cursor.execute("""insert into movie (length_in_minutes,name,release_date) values (%s, %s, %s) returning *;""", [length_in_minutes, name, release_date])
        return cursor.fetchone()

def remove_movie(movie_id):
    with get_db_cursor() as cursor:
        cursor.execute("""delete from movie where id=%s;""", [movie_id])
        return cursor.fetchone()

def get_movie(movie_id):
    with get_db_cursor() as cursor:
        cursor.execute("""select * from movie where id=%s;""", [movie_id])
        return cursor.fetchone()

def get_movies_showing():
    with get_db_cursor() as cursor:
        cursor.execute("""select movie_id from screening group by movie_id;""")
        return cursor.fetchall()

def get_screenings(movie_id):
    with get_db_cursor() as cursor:
        cursor.execute("""select * from screening where movie_id=%s;""", [movie_id])
        return cursor.fetchall()

def room_get_seats(screening_id, room_id):
     with get_db_cursor() as cursor:
        cursor.execute("""select *,(select id from ticket where ticket.seat_id = seat.id and booking_id = (select id from booking where screening_id = '%s')) from seat where room_id='%s'""", [screening_id, room_id])
        return cursor.fetchall()
        
def create_booking(customer_id, screening_id):
    with get_db_cursor() as cursor:
        cursor.execute("""insert into booking (screening_id, customer_id) values (%s,%s) returning booking_reference;""", [screening_id, customer_id])
        return cursor.fetchone()
