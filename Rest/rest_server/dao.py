from contextlib import contextmanager
import psycopg2
from psycopg2.extras import RealDictCursor
import posters


def get_db_connection():
    return psycopg2.connect(
        "host=localhost dbname=cinema_reservation_db user=postgres password=tomturbo"
    )

@contextmanager
def get_db_cursor():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        yield cursor
    finally:
        conn.commit()
        cursor.close()


def get_all_movies():
    with get_db_cursor() as cursor:
        cursor.execute("""select * from movie;""")
        return cursor.fetchall()


def get_movie_by_name(name):
    with get_db_cursor() as cursor:
        cursor.execute("""select * from movie where name=%s;""", [name])
        return cursor.fetchone()


def get_movies_by_year(release_date):
    with get_db_cursor() as cursor:
        cursor.execute("""select * from movie where release_date=%s;""",
                       [release_date])
        return cursor.fetchall()


def add_movie(length_in_minutes, name, release_date):
    with get_db_cursor() as cursor:
        cursor.execute(
            """insert into movie (length_in_minutes,name,release_date) values (%s, %s, %s) returning *;""",
            [length_in_minutes, name, release_date])
        movie = cursor.fetchone()
        posters.get_poster(movie)
        return movie


def remove_movie(movie_id):
    with get_db_cursor() as cursor:
        cursor.execute("""delete from movie where id=%s;""", [movie_id])


def get_movie(movie_id):
    with get_db_cursor() as cursor:
        cursor.execute("""select * from movie where id=%s;""", [movie_id])
        return cursor.fetchone()


def get_all_rooms():
    with get_db_cursor() as cursor:
        cursor.execute("""select * from room;""")
        return cursor.fetchall()


def get_all_cinemas():
    with get_db_cursor() as cursor:
        cursor.execute("""select * from cinema;""")
        return cursor.fetchall()


def get_movies_showing():
    with get_db_cursor() as cursor:
        cursor.execute(
            """select * from movie where id in (select movie_id from screening);"""
        )
        return cursor.fetchall()


def get_screenings(movie_id):
    with get_db_cursor() as cursor:
        cursor.execute("""select * from screening where movie_id=%s;""",
                       [movie_id])
        return cursor.fetchall()


def room_get_seats(screening_id, room_id):
    with get_db_cursor() as cursor:
        cursor.execute(
            """select *,(select id from ticket where ticket.seat_id = seat.id and booking_id = (select id from booking where screening_id = %s)) from seat where room_id=%s""",
            [screening_id, room_id])
        return cursor.fetchall()


def create_booking(customer_id, screening_id):
    with get_db_cursor() as cursor:
        cursor.execute(
            """insert into booking (screening_id, customer_id) values (%s,%s) returning *;""",
            [screening_id, customer_id])
        return cursor.fetchone()


def create_ticket(booking_id, seat_id):
    with get_db_cursor() as cursor:
        cursor.execute(
            """insert into ticket (booking_id, seat_id) values (%s,%s) returning id;""",
            [booking_id, seat_id])
        return cursor.fetchone()


def create_room(cinema_id, number):
    with get_db_cursor() as cursor:
        cursor.execute(
            """insert into room (cinema_id, number) values (%s,%s) returning id;""",
            [cinema_id, number])
        return cursor.fetchone()


def delete_room(room_id):
    with get_db_cursor() as cursor:
        cursor.execute("""delete from room where id=%s;""", [room_id])


def get_all_screenings():
    with get_db_cursor() as cursor:
        cursor.execute("""select * from screening;""")
        return cursor.fetchall()


def get_all_users():
    with get_db_cursor() as cursor:
        cursor.execute("""select * from users;""")
        return cursor.fetchall()