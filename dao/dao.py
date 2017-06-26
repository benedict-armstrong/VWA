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

def remove_movie(id):
    with get_db_cursor() as cursor:
        cursor.execute("""delete from movie where i;""", [length_in_minutes, name, release_date])
        return cursor.fetchone()

def add_movie(length_in_minutes, name, release_date):
    with get_db_cursor() as cursor:
        cursor.execute("""insert into movie (length_in_minutes,name,release_date) values (%s, %s, %s) returning *;""", [length_in_minutes, name, release_date])
        return cursor.fetchone()